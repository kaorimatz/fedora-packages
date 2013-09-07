%define relabel_files \
restorecon -R %{_bindir}/wpa_actiond; \
restorecon -R %{_sysconfdir}/wpa_actiond;

Name: wpa_actiond
Version: 1.4
Release: 1%{?dist}
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
Requires: %{name} = %{version}-%{release}
Requires: policycoreutils, libselinux-utils
Requires(post): selinux-policy-base >= %{_selinux_policy_version}, policycoreutils
Requires(post): %{name} = %{version}-%{release}
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
%{__make} %{?_smp_mflags}
%{__make} -f %{_datadir}/selinux/devel/Makefile


%install
install -D %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_sysconfdir}/%{name}

install -D %{name}.pp %{buildroot}%{_datadir}/selinux/packages/%{name}.pp
install -D %{name}.if %{buildroot}%{_datadir}/selinux/devel/include/contrib/%{name}.if


%post selinux
semodule -n -i %{_datadir}/selinux/packages/%{name}.pp
if /usr/sbin/selinuxenabled ; then
  /usr/sbin/load_policy
  %relabel_files
fi;
exit 0


%postun selinux
if [ $1 -eq 0 ]; then
  semodule -n -r %{name}
  if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    %relabel_files
  fi;
fi;
exit 0


%files
%doc COPYING
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/%{name}

%files selinux
%{_datadir}/selinux/packages/%{name}.pp
%{_datadir}/selinux/devel/include/contrib/%{name}.if


%changelog
* Sat Sep 07 2013 kaorimatz <kaorimatz@gmail.com> 1.4-1
* Initial package
