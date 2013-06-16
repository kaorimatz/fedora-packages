Name: yaskkserv
Version: 0.5.4
Release: 1%{?dist}
Summary: Yet Another SKK server

License: GPLv2+
URL: http://umiushi.org/~wac/yaskkserv/
Source0: http://umiushi.org/~wac/%{name}/%{name}-%{version}.tar.bz2

BuildRequires: perl
%if 0%{?fedora} != 17
BuildRequires: skkdic
%endif
BuildRequires: gcc-c++

%description
yaskkserv is a dictionary server for the SKK Japanese input method system.


%prep
%setup -q


%build
%configure --enable-google-japanese-input
make %{?_smp_mflags}


%install
make PREFIX=%{buildroot}%{_prefix} install_all

mv %{buildroot}%{_sbindir}/%{name}_* %{buildroot}%{_bindir}

%if 0%{?fedora} != 17
install -d %{buildroot}%{_datadir}/skk
%{buildroot}%{_bindir}/yaskkserv_make_dictionary \
    %{_datadir}/skk/SKK-JISYO.L \
    %{buildroot}%{_datadir}/skk/SKK-JISYO.L.yaskkserv
%endif


%files
%doc COPYING README.TXT documentation/*
%{_bindir}/%{name}_*
%if 0%{?fedora} != 17
%{_datadir}/skk/SKK-JISYO.L.yaskkserv
%endif


%changelog
* Sun Jun 16 2013 kaorimatz <kaorimatz@gmail.com> 0.5.4-1
- Initial package
