#
# Conditional build:
%bcond_without	gconf		# gconf plugin
%bcond_without	gtk		# gtk window decorator
%bcond_without	gnome		# gnome settings module
%bcond_without	metacity	# metacity theme support
%bcond_without	kde		# kde-window-decorator
#
Summary:	OpenGL window and compositing manager
Summary(pl.UTF-8):	OpenGL-owy zarządca okien i składania
Name:		compiz
Version:	0.5.2
Release:	3
License:	GPL or MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.gz
# Source0-md5:	7a38a921359573fb57d53e057f481f08
Patch0:		%{name}-DESTDIR.patch
URL:		http://xorg.freedesktop.org/
%if %{with gconf} || %{with gtk}
BuildRequires:	GConf2-devel >= 2.0
%endif
BuildRequires:	Mesa-libGL-devel >= 6.5-1.20060411.2
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.0
BuildRequires:	dbus-devel >= 0.35
BuildRequires:	glib2-devel >= 2.0
# <sys/inotify.h>
BuildRequires:	glibc-devel >= 6:2.4
BuildRequires:	glitz-devel
BuildRequires:	intltool
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.14.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel >= 0.7
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXres-devel
%if %{with gtk}
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	libwnck-devel >= 2.14.1-2
BuildRequires:	pango-devel >= 1.10.0
BuildRequires:	xorg-lib-libXrender-devel >= 0.8.4
%if %{with gnome}
BuildRequires:	control-center-devel >= 2.0
BuildRequires:	gnome-desktop-devel >= 2.0
BuildRequires:	gnome-menus-devel
%endif
%if %{with metacity}
BuildRequires:	metacity-devel >= 2.15.21
%endif
%endif
%if %{with kde}
BuildRequires:	dbus-qt-devel
BuildRequires:	kdelibs-devel
BuildRequires:	kdebase-devel
BuildRequires:	qt-devel >= 1:3.0
%endif
Conflicts:	xorg-xserver-xgl < 0.0.20060505
Obsoletes:	compiz-opacity
Obsoletes:	beryl-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compiz is a compositing window manager that uses 3D graphics
acceleration via OpenGL. It provides various new graphical effects
and features on any desktop environment, including Gnome and KDE.

%description -l pl.UTF-8
Compiz jest menedżerem okien obsługującym składanie, który używa
akceleracji grafiki 3D przez OpenGL-a. Umożliwia on uzyskanie nowych
efektów graficznych i możliwości w dowolnym środowisku, nie
wyłączając Gnome i KDE.

%package libs
Summary:	Compiz libraries
Summary(pl.UTF-8):	Biblioteki compiza
Group:		X11/Applications

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

%package gconf
Summary:	GConf plugin for Compiz
Summary(pl.UTF-8):	Wtyczka GConf dla Compiza
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires:	%{name} = %{version}-%{release}
Obsoletes:	beryl-core-gconf

%description gconf
GConf plugin for Compiz.

%description gconf -l pl.UTF-8
Wtyczka GConf dla Compiza.

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

%description gtk-decorator
Window decorator for GTK+.

%description gtk-decorator -l pl.UTF-8
Dekorator okien dla GTK+.

%package kde-decorator
Summary:	Window decorator for KDE
Summary(pl.UTF-8):	Dekorator okien dla KDE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description kde-decorator
Window decorator for KDE.

%description kde-decorator -l pl.UTF-8
Dekorator okien dla KDE.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
QTLIB=%{_libdir}; export QTLIB
%configure \
	--disable-static \
	--enable-librsvg \
	%{!?with_gconf:--disable-gconf} \
	%{!?with_gnome:--disable-gnome} \
	%{!?with_gtk:--disable-gtk} \
	%{!?with_kde:--disable-kde} \
	%{!?with_metacity:--disable-metacity}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	desktopfilesdir=%{_datadir}/wm-properties \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/compiz/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post gconf
%gconf_schema_install

%preun gconf
%gconf_schema_uninstall

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
%{?with_gconf:%exclude %{_libdir}/compiz/libgconf.so}
%{_datadir}/compiz
%{?with_gconf:%exclude %{_datadir}/compiz/gconf.xml}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdecoration.so.*.*.*
%dir %{_libdir}/compiz

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdecoration.so
%{_libdir}/libdecoration.la
%{_includedir}/compiz
%{_pkgconfigdir}/compiz.pc
%{_pkgconfigdir}/libdecoration.pc
# what is the purpose of these files? development or runtime?
%{_pkgconfigdir}/compiz-cube.pc
%{_pkgconfigdir}/compiz-scale.pc

%if %{with gconf}
%files gconf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/compiz/libgconf.so
%{_sysconfdir}/gconf/schemas/compiz-*.schemas
%{_datadir}/compiz/gconf.xml
# what for?
%{_pkgconfigdir}/compiz-gconf.pc
%endif

%if %{with gnome}
%files gnome-settings
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/window-manager-settings/*.so
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
