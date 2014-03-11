%global relabel_files \
restorecon -R %{_bindir}/netctl; \
restorecon -R %{_bindir}/netctl-auto; \
restorecon -R %{_libexecdir}/netctl; \
restorecon -R %{_localstatedir}/run/netctl; \
restorecon -R %{_unitdir}/netctl*;

Name: netctl
Version: 1.4
Release: 2%{?dist}
License: GPLv3+
URL: https://projects.archlinux.org/netctl.git
Summary: Profile based systemd network management

Source0: ftp://ftp.archlinux.org/other/packages/%{name}/%{name}-%{version}.tar.xz
Source1: %{name}.te
Source2: %{name}.if
Source3: %{name}.fc
Patch0: %{name}-%{version}-ctrl-interface.patch
Patch1: %{name}-%{version}-wpa_actiond-action-script.patch

BuildArch: noarch
BuildRequires: asciidoc
Requires: dhclient
Requires: iproute
Requires: wpa_supplicant
Requires: wpa_actiond
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%package selinux
Summary: SELinux policy module for %{name}

BuildArch: noarch
BuildRequires: selinux-policy-devel
BuildRequires: wpa_actiond-selinux
Requires: %{name} = %{version}-%{release}
Requires: selinux-policy >= %{_selinux_policy_version}
Requires(post): libselinux-utils
Requires(post): policycoreutils
Requires(postun): libselinux-utils
Requires(postun): policycoreutils


%description
netctl is a profile based systemd network management.

%description selinux
This package installs and sets up the SELinux policy security module for netctl.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
find -type f | xargs sed -i 's,/usr/lib/network,%{_libexecdir}/%{name},g'
find -type f | xargs sed -i 's,/run/network,/run/%{name},g'
find -type f | xargs sed -i 's,/usr/bin/ifplugd,%{_sbindir}/ifplugd,g'

cp %{SOURCE1} %{SOURCE2} %{SOURCE3} .


%build
%{__make} -f %{_datadir}/selinux/devel/Makefile


%install
make DESTDIR=%{buildroot} install

rm -r %{buildroot}%{_sysconfdir}/%{name}/examples

install -D -m 644 contrib/bash-completion %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}
install -D -m 644 contrib/zsh-completion %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -D -m 755 %{buildroot}%{_libexecdir}/%{name}/auto.action %{buildroot}%{_sysconfdir}/wpa_actiond/%{name}.action

install -D -m 644 %{name}.pp %{buildroot}%{_datadir}/selinux/packages/%{name}.pp
install -D -m 644 %{name}.if %{buildroot}%{_datadir}/selinux/devel/include/contrib/%{name}.if


%files
%doc AUTHORS NEWS README docs/examples
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/*
%{_datadir}/zsh/site-functions/_%{name}
%{_libexecdir}/%{name}
%{_mandir}/man[157]/*
%{_sysconfdir}/bash_completion.d/%{name}
%{_sysconfdir}/ifplugd/%{name}.action
%{_sysconfdir}/wpa_actiond/%{name}.action
%{_unitdir}/*

%files selinux
%{_datadir}/selinux/packages/%{name}.pp
%{_datadir}/selinux/devel/include/contrib/%{name}.if


%post
%systemd_post netctl

%post selinux
semodule -n -i %{_datadir}/selinux/packages/%{name}.pp
if /usr/sbin/selinuxenabled; then
  /usr/sbin/load_policy
  %relabel_files
fi


%preun
if [ $1 -eq 0 ]; then
  /usr/bin/netctl stop-all > /dev/null 2>&1 || :
fi


%postun
/usr/bin/systemctl daemon-reload > /dev/null 2>&1 || :
if [ $1 -ge 1 ]; then
  /usr/bin/netctl store > /dev/null 2>&1 || :
  /usr/bin/netctl stop-all > /dev/null 2>&1 || :
  /usr/bin/netctl restore > /dev/null 2>&1 || :
fi

%postun selinux
if [ $1 -eq 0 ]; then
  semodule -n -r %{name}
  if /usr/sbin/selinuxenabled; then
    /usr/sbin/load_policy
    %relabel_files
  fi
fi


%changelog
* Tue Feb 11 2014 Satoshi Matsumoto <kaorimatz@gmail.com> - 1.4-2
- Fix license to GPLv3+
- Fix URL

* Fri Nov 29 2013 kaorimatz <kaorimatz@gmail.com> - 1.4-1
- Upgrade to upstream version 1.4
- Remove ifplugd from dependencies

* Fri Nov 29 2013 kaorimatz <kaorimatz@gmail.com> - 1.3-3
- Add SELinux policy
- Fix to install auto.action

* Sat Sep 07 2013 kaorimatz <kaorimatz@gmail.com> - 1.3-2
- Require wpa_actiond

* Sun Aug 11 2013 kaorimatz <kaorimatz@gmail.com> - 1.3-1
- Upgrade to upstream version 1.3

* Sat Jul 27 2013 kaorimatz <kaorimatz@gmail.com> - 1.2-1
- Upgrade to upstream version 1.2
- Remove -examples patch

* Sun Jun 16 2013 kaorimatz <kaorimatz@gmail.com> - 1.1-1
- Upgrade to upstream version 1.1
- Add missing requires on systemd

* Sun May 19 2013 kaorimatz <kaorimatz@gmail.com> - 1.0-1
- Initial package
