%define checkout 20131221git5ed5e90

Name: dmenu-xft
Version: 4.5
Release: 0.1.%{checkout}%{?dist}
License: MIT
URL: http://tools.suckless.org/dmenu/
Summary: Dynamic menu for X

Source0: dmenu-%{checkout}.tar.bz2
Patch0: https://gist.github.com/kaorimatz/8057265/raw/274d50fed69faaffe15f9d7270a14867f935cc7a/dmenu-git5ed5e90-xft.diff
Patch1: dmenu-20131221git5ed5e90-make.patch

BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXinerama-devel


%description
dmenu is a dynamic menu for X, originally designed for dwm. It manages large
numbers of user-defined menu items efficiently.

Built with support for Xft.


%prep
%setup -q -n dmenu-%{checkout}
%patch0 -p1
%patch1 -p1


%build
%{__make} XFTINC="$(pkg-config --cflags xft)" XFTLIBS="$(pkg-config --libs xft)"


%install
%{makeinstall} DESTDIR=%{buildroot} PREFIX=%{_prefix}


%files
%doc LICENSE Makefile README
%{_bindir}/dmenu
%{_bindir}/dmenu_path
%{_bindir}/dmenu_run
%{_bindir}/stest
%{_mandir}/man1/dmenu.1.*
%{_mandir}/man1/stest.1.*


%changelog
* Sat Dec 21 2013 kaorimatz <kaorimatz@gmail.com> - 4.5-0.1.20131221git5ed5e90
- Initial package
