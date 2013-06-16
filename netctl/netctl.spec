Name: netctl
Version: 1.1
Release: 1%{?dist}
Summary: Profile based systemd network management

License: GPLv2+
URL: http://projects.archlinux.org/netctl.git/
Source0: ftp://ftp.archlinux.org/other/packages/%{name}/%{name}-%{version}.tar.xz
Patch0: %{name}-%{version}-ctrl-interface.patch
Patch1: %{name}-%{version}-examples.patch

BuildArch: noarch
BuildRequires: asciidoc
Requires: dhclient,ifplugd,iproute,wpa_supplicant
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Netctl is a profile based systemd network management.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
find -type f | xargs sed -i "s|/usr/lib/network|%{_libexecdir}/%{name}|g"


%build


%install
make DESTDIR=%{buildroot} install

install -D -m 644 contrib/bash-completion %{buildroot}/%{_sysconfdir}/bash_completion.d/%{name}
install -D -m 644 contrib/zsh-completion %{buildroot}/%{_datadir}/zsh/site-functions/_%{name}


%files
%doc AUTHORS NEWS README docs/examples
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/*
%{_datadir}/zsh/site-functions/_%{name}
%{_libexecdir}/%{name}
%{_mandir}/man[157]/*
%{_sysconfdir}/bash_completion.d/%{name}
%{_sysconfdir}/ifplugd/*
%{_unitdir}/*


%post
%systemd_post netctl


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


%changelog
* Sun Jun 16 2013 kaorimatz <kaorimatz@gmail.com> 1.1-1
- Upgrade to upstream version 1.1
- Add missing requires on systemd

* Sun May 19 2013 kaorimatz <kaorimatz@gmail.com> 1.0-1
- Initial package
