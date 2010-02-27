#
# Conditional build:
%bcond_without	gconf		# gconf plugin
%bcond_without	gtk		# gtk window decorator
%bcond_without	gnome		# gnome settings module
%bcond_without	metacity	# metacity theme support
%bcond_with	kde		# kde-window-decorator and kconfig
%bcond_without	kde4		# kde4-window-decorator
#
Summary:	OpenGL window and compositing manager
Summary(pl.UTF-8):	OpenGL-owy zarządca okien i składania
Name:		compiz
# note that even versions are STABLE
Version:	0.8.4
Release:	4
License:	GPL or MIT
Group:		X11/Applications
Source0:	http://releases.compiz.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	03fa78ce0c464f3a413b2a3b74f09559
Patch0:		%{name}-kde4.patch
Patch1:		%{name}-libpng14.patch
Patch2:		%{name}-kde44-api.patch
URL:		http://www.compiz.org/
%if %{with gconf} || %{with gtk}
BuildRequires:	GConf2-devel >= 2.0
%endif
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel >= 2.1
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7
BuildRequires:	cairo-devel >= 1.0
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0
# <sys/inotify.h>
BuildRequires:	glibc-devel >= 6:2.4
BuildRequires:	intltool >= 0.23
BuildRequires:	libfuse-devel >= 2.2
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1:2.14.0
BuildRequires:	libtool
BuildRequires:	libxcb-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel >= 0.7
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel >= 0.9.3
BuildRequires:	xorg-lib-libXres-devel
%if %{with gtk}
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	libwnck-devel >= 2.20.0
%if %{with gnome}
BuildRequires:	gnome-control-center-devel >= 2.0
BuildRequires:	gnome-desktop-devel >= 2.0
BuildRequires:	gnome-menus-devel
%endif
%if %{with metacity}
BuildRequires:	metacity-devel >= 2.24.0
%endif
%endif
%if %{with kde}
BuildRequires:	dbus-qt-devel
BuildRequires:	kdebase-devel
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel >= 1:3.0
%endif
%if %{with kde4}
BuildRequires:	kde4-kdebase-workspace-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	qt4-build
%endif
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	compiz-opacity
Conflicts:	filesystem < 3.0-20
Conflicts:	xorg-xserver-xgl < 0.0.20060505
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# for gconf subpackage
%define	plugins annotate blur clone core cube dbus decoration fade fs gconf glib gnomecompat ini inotify minimize move obs place png regex resize rotate scale screenshot svg switcher video water wobbly zoom

%description
Compiz is a compositing window manager that uses 3D graphics
acceleration via OpenGL. It provides various new graphical effects and
features on any desktop environment, including Gnome and KDE.

%description -l pl.UTF-8
Compiz jest menedżerem okien obsługującym składanie, który używa
akceleracji grafiki 3D przez OpenGL-a. Umożliwia on uzyskanie nowych
efektów graficznych i możliwości w dowolnym środowisku, nie wyłączając
Gnome i KDE.

%package libs
Summary:	Compiz libraries
Summary(pl.UTF-8):	Biblioteki compiza
Group:		X11/Applications
Obsoletes:	beryl-core
Conflicts:	compiz < 0.5.2-2

%description libs
Compiz libraries.

%description libs -l pl.UTF-8
Biblioteki Compiza.

%package devel
Summary:	Header files for compiz
Summary(pl.UTF-8):	Pliki nagłówkowe dla compiza
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
# (by compiz.pc; header requires only: OpenGL-devel, startup-notification-devel, damageproto, xextproto, libX11-devel)
Requires:	OpenGL-devel
Requires:	libpng-devel
Requires:	libxslt-devel
Requires:	startup-notification-devel >= 0.7
Requires:	xorg-lib-libSM-devel
Requires:	xorg-lib-libXcomposite-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXinerama-devel
Requires:	xorg-lib-libXrandr-devel
Obsoletes:	beryl-core-devel

%description devel
Header files for compiz.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla compiza.

%package fuse
Summary:	FUSE plugin for Compiz
Summary(pl.UTF-8):	Wtyczka FUSE dla Compiza
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description fuse
FUSE plugin for Compiz (userspace file system).

%description fuse -l pl.UTF-8
Wtyczka FUSE dla Compiza (system plików w przestrzeni użytkownika).

%package gconf
Summary:	GConf plugin for Compiz
Summary(pl.UTF-8):	Wtyczka GConf dla Compiza
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires:	%{name} = %{version}-%{release}
Obsoletes:	beryl-core-gconf

%description gconf
GConf plugin for Compiz (GConf control backend).

%description gconf -l pl.UTF-8
Wtyczka GConf dla Compiza (backend sterujący oparty na GConfie).

%package kconfig
Summary:	kconfig plugin for Compiz
Summary(pl.UTF-8):	Wtyczka kconfig dla Compiza
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description kconfig
kconfig plugin for Compiz (KDE control backend).

%description kconfig -l pl.UTF-8
Wtyczka kconfig dla Compiza (backend sterujący oparty na KDE).

%package svg
Summary:	SVG plugin for Compiz
Summary(pl.UTF-8):	Wtyczka SVG dla Compiza
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description svg
SVG image loader plugin for Compiz.

%description svg -l pl.UTF-8
Wtyczka wczytująca obrazy SVG dla Compiza.

%package gnome-settings
Summary:	Compiz settings for GNOME control panel
Summary(pl.UTF-8):	Ustawienia compiza dla panelu sterowania GNOME
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description gnome-settings
Compiz settings for GNOME control panel.

%description gnome-settings -l pl.UTF-8
Ustawienia compiza dla panelu sterowania GNOME.

%package gtk-decorator
Summary:	Window decorator for GTK+
Summary(pl.UTF-8):	Dekorator okien dla GTK+
Group:		X11/Applications
%if %{with gconf}
Requires(post,preun):	GConf2
%endif
Requires:	%{name} = %{version}-%{release}
Obsoletes:	compiz-gnome-decorator
Obsoletes:	heliodor

%description gtk-decorator
Window decorator for GTK+.

%description gtk-decorator -l pl.UTF-8
Dekorator okien dla GTK+.

%package kde-decorator
Summary:	Window decorator for KDE
Summary(pl.UTF-8):	Dekorator okien dla KDE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	aquamarine

%description kde-decorator
Window decorator for KDE.

%description kde-decorator -l pl.UTF-8
Dekorator okien dla KDE.

%package kde4-decorator
Summary:	Window decorator for KDE 4
Summary(pl.UTF-8):	Dekorator okien dla KDE 4
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	aquamarine

%description kde4-decorator
Window decorator for KDE 4.

%description kde4-decorator -l pl.UTF-8
Dekorator okien dla KDE 4.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
QTLIB=%{_libdir}; export QTLIB
QTDIR=%{_prefix}; export QTDIR
%configure \
	--disable-static \
	--enable-librsvg \
	%{!?with_gconf:--disable-gconf} \
	%{!?with_gnome:--disable-gnome} \
	%{!?with_gtk:--disable-gtk} \
	%{!?with_kde:--disable-kde} \
	%{!?with_kde4:--disable-kde4} \
	%{!?with_metacity:--disable-metacity}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/compiz/*.la
%if %{with gnome}
rm -f $RPM_BUILD_ROOT%{_libdir}/window-manager-settings/*.la
%endif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post gconf
for p in %{plugins}; do
	%gconf_schema_install compiz-$p.schemas
done

%preun gconf
for p in %{plugins}; do
	%gconf_schema_uninstall compiz-$p.schemas
done

%if %{with gconf}
%post gtk-decorator
%gconf_schema_install gwd.schemas

%preun gtk-decorator
%gconf_schema_uninstall gwd.schemas
%endif

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING.MIT ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/compiz
%attr(755,root,root) %{_libdir}/compiz/*.so
%exclude %{_libdir}/compiz/libfs.so
%{?with_kde:%exclude %{_libdir}/compiz/libkconfig.so}
%{?with_gconf:%exclude %{_libdir}/compiz/libgconf.so}
%exclude %{_libdir}/compiz/libsvg.so
%{_datadir}/compiz/*.xml
%{_datadir}/compiz/*.png
%{_datadir}/compiz/schemas.xslt
%exclude %{_datadir}/compiz/fs.xml
%exclude %{_datadir}/compiz/gconf.xml
%exclude %{_datadir}/compiz/svg.xml

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdecoration.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdecoration.so.0
%dir %{_libdir}/compiz
%dir %{_datadir}/compiz

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdecoration.so
%{_libdir}/libdecoration.la
%{_includedir}/compiz
%{_pkgconfigdir}/compiz.pc
%{_pkgconfigdir}/libdecoration.pc
%{?with_kde:%{_pkgconfigdir}/compiz-kconfig.pc}
# checked by compiz-fusion-plugins-extra
%{_pkgconfigdir}/compiz-cube.pc
# checked by compiz-fusion-plugins-main
%{_pkgconfigdir}/compiz-scale.pc

%files fuse
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/compiz/libfs.so
%{_datadir}/compiz/fs.xml

%if %{with gconf}
%files gconf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/compiz/libgconf.so
%{_sysconfdir}/gconf/schemas/compiz-*.schemas
%{_datadir}/compiz/gconf.xml
# checked by compiz-fusion-plugins-* (with non-default --enable-schemas only)
%{_pkgconfigdir}/compiz-gconf.pc
%endif

%if %{with kde}
%files kconfig
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/compiz/libkconfig.so
%{_datadir}/config/compizrc
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/compiz/kcfg.xslt
%{_datadir}/compiz/kconfig.xslt
%endif

%files svg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/compiz/libsvg.so
%{_datadir}/compiz/gconf.xml

%if %{with gnome} && %{with gtk}
%files gnome-settings
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/window-manager-settings/libcompiz.so
%{_datadir}/gnome-control-center/keybindings/50-compiz-desktop-key.xml
%{_datadir}/gnome-control-center/keybindings/50-compiz-key.xml
%{_datadir}/gnome/wm-properties/compiz-wm.desktop
%{_desktopdir}/compiz.desktop
%endif

%if %{with gtk}
%files gtk-decorator
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtk-window-decorator
%if %{with gconf}
%{_sysconfdir}/gconf/schemas/gwd.schemas
%endif
%endif

%if %{with kde}
%files kde-decorator
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kde-window-decorator
%endif

%if %{with kde4}
%files kde4-decorator
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kde4-window-decorator
%endif
