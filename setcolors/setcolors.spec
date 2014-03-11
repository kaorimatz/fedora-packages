%global checkout 20131109git909f310


Name: setcolors
Version: 0.0.0
Release: 0.2.%{checkout}%{?dist}
License: MIT
URL: https://github.com/EvanPurkhiser/linux-vt-setcolors
Summary: Utility tool to set the Linux VT default color palette

Source0: %{name}-%{checkout}.tar.bz2
Patch0: %{name}-%{checkout}-compiler-flags.patch


%description
setcolors is a little utility to change the default color palette of the Linux
VT101 virtual console. The program accepts a configuration file containing the
colors in hexadecimal form to use.


%prep
%setup -q -n %{name}-%{checkout}
%patch0 -p1


%build
%{__make} %{_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%install
%{make_install} PREFIX=%{_prefix}


%files
%doc LICENSE Makefile README.md
%{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}


%changelog
* Sun Dec 01 2013 kaorimatz <kaorimatz@gmail.com> - 0.0.0-0.2.20131109git909f310
- Build with $RPM_OPT_FLAGS and $RPM_LD_FLAGS

* Sat Nov 09 2013 kaorimatz <kaorimatz@gmail.com> - 0.0.0-0.1.20131109git909f310
- Initial package
