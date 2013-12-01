%global relabel_files \
restorecon -R %{_bindir}/wpa_actiond; \
restorecon -R %{_sysconfdir}/wpa_actiond;

Name: wpa_actiond
Version: 1.4
Release: 3%{?dist}
License: GPLv2
URL: http://projects.archlinux.org/wpa_actiond.git/
Summary: Connect to wpa_supplicant and handle connect and disconnect events

Source0: ftp://ftp.archlinux.org/other/wpa_actiond/%{name}-%{version}.tar.xz
Source1: %{name}.te
Source2: %{name}.if
Source3: %{name}.fc

Requires: wpa_supplicant

%package selinux
Summary: SELinux policy module for %{name}

BuildArch: noarch
BuildRequires: selinux-policy-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: selinux-policy >= %{_selinux_policy_version}
Requires(post): libselinux-utils
Requires(post): policycoreutils
Requires(postun): libselinux-utils
Requires(postun): policycoreutils


%description
%{name} is a daemon that connects to wpa_supplicant and handles connect and
disconnect events.

%description selinux
This package installs and sets up the SELinux policy security module for
%{name}.


%prep
%setup -q

cp %{SOURCE1} %{SOURCE2} %{SOURCE3} .


%build
%{__make} %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%{__make} -f %{_datadir}/selinux/devel/Makefile


%install
install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_sysconfdir}/%{name}

install -D -m 644 %{name}.pp %{buildroot}%{_datadir}/selinux/packages/%{name}.pp
install -D -m 644 %{name}.if %{buildroot}%{_datadir}/selinux/devel/include/contrib/%{name}.if


%post selinux
semodule -n -i %{_datadir}/selinux/packages/%{name}.pp
if /usr/sbin/selinuxenabled; then
  /usr/sbin/load_policy
  %relabel_files
fi


%postun selinux
if [ $1 -eq 0 ]; then
  semodule -n -r %{name}
  if /usr/sbin/selinuxenabled; then
    /usr/sbin/load_policy
    %relabel_files
  fi
fi


%files
%doc COPYING
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/%{name}

%files selinux
%{_datadir}/selinux/packages/%{name}.pp
%{_datadir}/selinux/devel/include/contrib/%{name}.if


%changelog
* Sun Dec 01 2013 kaorimatz <kaorimatz@gmail.com> 1.4-3
* Build with $RPM_OPT_FLAGS and $RPM_LD_FLAGS

* Fri Nov 29 2013 kaorimatz <kaorimatz@gmail.com> 1.4-2
- Fix SELinux policy with regard to netctl
- Fix wrong permissions
- Fix wrong dependencies for the SElinux policy module

* Sat Sep 07 2013 kaorimatz <kaorimatz@gmail.com> 1.4-1
- Initial package
