Name: wrk
Version: 3.0.3
Release: 1%{?dist}
License: ASL 2.0
URL: https://github.com/wg/wrk
Summary: Modern HTTP benchmarking tool

Source0: https://github.com/wg/%{name}/archive/%{version}.tar.gz

BuildRequires: openssl-devel


%description
wrk is a modern HTTP benchmarking tool capable of generating significant load
when run on a single multi-core CPU. It combines a multithreaded design with
scalable event notification systems such as epoll and kqueue.


%prep
%setup -q


%build
make


%install
install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}


%files
%doc LICENSE Makefile
%{_bindir}/%{name}


%changelog
* Tue Nov 12 2013 kaorimatz <kaorimatz@gmail.com> 3.0.3-1
* Upgrade to upstream version 3.0.3
* Tue Oct 01 2013 kaorimatz <kaorimatz@gmail.com> 3.0.0-1
* Upgrade to upstream version 3.0.0
* Sat Jun 22 2013 kaorimatz <kaorimatz@gmail.com> 2.2.0-1
- Initial package
