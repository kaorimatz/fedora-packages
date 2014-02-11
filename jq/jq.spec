Name: jq
Version: 1.3
Release: 2%{?dist}
License: MIT
URL: http://stedolan.github.io/jq/
Summary: Command-line JSON processor

Source0: https://github.com/stedolan/%{name}/archive/%{name}-%{version}.tar.gz
Patch0: https://github.com/stedolan/%{name}/pull/175.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: flex
BuildRequires: valgrind


%description
%{name} is a lightweight and flexible command-line JSON processor.


%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1


%build
autoreconf --install
%{configure}
%{__make}


%install
%{make_install}


%check
%{__make} check


%files
%doc AUTHORS COPYING README README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Tue Feb 11 2014 Satoshi Matsumoto <kaorimatz@gmail.com> - 1.3-2
- Fix license to MIT

* Tue Nov 12 2013 kaorimatz <kaorimatz@gmail.com> - 1.3-1
- Initial package
