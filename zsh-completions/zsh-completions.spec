%global _python_bytecompile_errors_terminate_build 0

Name: zsh-completions
Version: 0.9.0
Release: 1%{?dist}
Summary: Additional completion definitions for Zsh

License: BSD
URL: https://github.com/zsh-users/zsh-completions
Source0: https://github.com/zsh-users/%{name}/archive/%{version}.tar.gz

BuildArch: noarch
Requires: zsh

%description
zsh-completions is a collection of new completion scripts that are not
available in Zsh yet.


%prep
%setup -q


%build


%install
install -d -m 755 %{buildroot}%{_datadir}/zsh/site-functions
install -m 644 src/_* %{buildroot}%{_datadir}/zsh/site-functions/


%files
%doc README.md
%{_datadir}/zsh/site-functions/_*


%changelog
* Sun Jun 23 2013 kaorimatz <kaorimatz@gmail.com> 0.9.0-1
- Initial package
