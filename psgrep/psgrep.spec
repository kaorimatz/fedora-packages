%global checkout 20130622git936fc18

Name: psgrep
Version: 1.0.7
Release: 0.1.%{checkout}%{?dist}
Summary: Process list searching via grep

License: GPLv3+
URL: https://github.com/jvz/psgrep
Source0: %{name}-%{checkout}.tar.bz2

BuildArch: noarch

%description
psgrep is a simple little shell script to help with the "ps aux | grep" idiom.


%prep
%setup -q -n %{name}-%{checkout}


%build


%install
PREFIX=%{buildroot}%{_prefix} ./install.sh


%files
%doc COPYING TODO ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Sat Jun 22 2013 kaorimatz <kaorimatz@gmail.com> - 1.0.7-0.1.20130622git936fc18
- Initial package
