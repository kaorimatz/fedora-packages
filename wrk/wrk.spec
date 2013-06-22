Name: wrk
Version: 2.2.0
Release: 1%{?dist}
Summary: Modern HTTP benchmarking tool

License: ASL 2.0
URL: https://github.com/wg/wrk
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
* Sat Jun 22 2013 kaorimatz <kaorimatz@gmail.com> 2.2.0-1
- Initial package
