Name: rfc
Version: 0.2.2
Release: 1%{?dist}
License: MIT
URL: https://github.com/bfontaine/rfc
Summary: Read RFCs from the command-line

Source0: https://github.com/bfontaine/%{name}/archive/v%{version}.tar.gz

BuildArch: noarch
BuildRequires: bc


%description
rfc is a little tool written in bash to read RFCs from the command-line.
It fetches RFCs and drafts from the Web and caches them locally.


%prep
%setup -q


%build


%install
install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}


%check
./test/tests.sh


%files
%doc README.md
%{_bindir}/%{name}


%changelog
* Sat Mar 01 2014 Satoshi Matsumoto <kaorimatz@gmail.com> - 0.2.2-1
- Initial package
