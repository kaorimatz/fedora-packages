Name: screenfetch
Version: 3.2.2
Release: 2%{?dist}
License: GPLv3+
URL: http://git.silverirc.com/cgit.cgi/screenfetch.git/
Summary: Bash screenshot info grabber

Source0: http://git.silverirc.com/cgit.cgi/%{name}.git/snapshot/%{name}-%{version}.tar.bz2

BuildArch: noarch
Requires: glx-utils
Requires: scrot
Requires: xorg-x11-utils


%description
screenfetch is a tool which fetches system/theme information in terminal for
Linux desktop screenshots.


%prep
%setup -q


%build


%install
install -D -m 755 %{name}-dev %{buildroot}%{_bindir}/%{name}


%files
%doc CHANGELOG COPYING README.mkdn TODO
%{_bindir}/%{name}


%changelog
* Tue Feb 11 2014 Satoshi Matsumoto <kaorimatz@gmail.com> - 3.2.2-2
- Fix license to GPLv3+

* Fri Nov 08 2013 kaorimatz <kaorimatz@gmail.com> - 3.2.2-1
- Upgrade to upstream version 3.2.2

* Tue Oct 01 2013 kaorimatz <kaorimatz@gmail.com> - 3.2.0-1
- Upgrade to upstream version 3.2.0

* Tue Sep 03 2013 kaorimatz <kaorimatz@gmail.com> - 3.1.0-1
- Upgrade to upstream version 3.1.0

* Sat Jul 27 2013 kaorimatz <kaorimatz@gmail.com> - 3.0.5-1
- Upgrade to upstream version 3.0.5

* Sun Jun 23 2013 kaorimatz <kaorimatz@gmail.com> - 3.0.0-1
- Initial package
