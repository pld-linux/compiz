#
# Conditional build:
%bcond_without	gconf		# don't build gconf plugin
%bcond_without	gnome		# don't build gnome-window-decorator
%bcond_without	kde		# dont' build kde-window-decorator
#
%define		_snap	20060331
#
Summary:	OpenGL window and compositing manager
Summary(pl):	OpenGL-owy zarz±dca okien i sk³adania
Name:		compiz
Version:	0.0.7
Release:	1.%{_snap}.1
License:	GPL/MIT
Group:		X11
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	b42d03bf0625cb32cd8f6f24a6028f2c
Patch0:		%{name}-switcher-all-desktops.patch
Patch1:		%{name}-minimize-scaler-mod.patch
%if %{with gconf} || %{with gnome}
BuildRequires:	GConf2-devel >= 2.0
%endif
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libpng-devel
BuildRequires:	libsvg-cairo-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel >= 0.7
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrandr-devel
%if %{with gnome}
BuildRequires:	control-center-devel >= 2.0
BuildRequires:	gnome-desktop-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	libwnck-devel >= 2.0
%endif
%if %{with kde}
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build
%endif
Obsoletes:	compiz-opacity
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compiz is an OpenGL compositing manager that use
GLX_EXT_texture_from_pixmap for binding redirected top-level
windows to texture objects. It has a flexible plug-in system
and it is designed to run well on most graphics hardware.

%description -l pl
Compiz jest OpenGL-owym zarz±dc± sk³adania, u¿ywaj±cym rozszerzenia
GLX_EXT_texture_from_pixmap w celu wi±zania przekierowanych okien
do tekstur. Posiada elastyczny system wtyczek i jest tak
zaprojektowany, by dobrze dzia³aæ na wiêkszo¶ci kart graficznych.

%package devel
Summary:	Header files for compiz
Summary(pl):	Pliki nag³ówkowe dla compiza
Group:		Development
# (by compiz.pc; header requires only: OpenGL-devel, startup-notification-devel, damageproto, xextproto, libX11-devel)
Requires:	OpenGL-devel
Requires:	libpng-devel
Requires:	startup-notification-devel >= 0.7
Requires:	xorg-lib-libSM-devel
Requires:	xorg-lib-libXcomposite-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXrandr-devel

%description devel
Header files for compiz.

%description devel -l pl
Pliki nag³ówkowe dla compiza.

%package gnome-settings
Summary:	Compiz settings for gnome control panel
Summary(pl):	Ustawienia compiza dla panelu sterowania gnome
Group:		X11
Requires:	%{name} = %{version}-%{release}

%description gnome-settings
Compiz settings for gnome control panel.

%description gnome-settings -l pl
Ustawienia compiza dla panelu sterowania gnome.

%package gnome-decorator
Summary:	Window decorator for gnome
Summary(pl):	Dekorator okien dla gnome
Group:		X11
Requires:	%{name} = %{version}-%{release}

%description gnome-decorator
Window decorator for gnome.

%description gnome-decorator -l pl
Dekorator okien dla gnome.

%package kde-decorator
Summary:	Window decorator for KDE
Summary(pl):	Dekorator okien dla KDE
Group:		X11
Requires:	%{name} = %{version}-%{release}

%description kde-decorator
Window decorator for KDE.

%description kde-decorator -l pl
Dekorator okien dla KDE.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p0

%build
autoreconf -v --install

%configure \
	--disable-static \
	--enable-svg \
	--enable-libsvg-cairo \
	%{!?with_gconf:--disable-gconf} \
	--%{?with_gnome:en}%{!?with_gnome:dis}able-gnome \
	--%{?with_kde:en}%{!?with_kde:dis}able-kde

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/compiz/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/compiz
%dir %{_libdir}/compiz
%attr(755,root,root) %{_libdir}/compiz/*.so
%{_datadir}/compiz
%if %{with gnome}
%{_datadir}/gnome/wm-properties/*
%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/compiz
%{_pkgconfigdir}/compiz.pc

%if %{with gnome}
%files gnome-settings
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/window-manager-settings/*.so

%files gnome-decorator
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-window-decorator
%endif

%if %{with kde}
%files kde-decorator
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kde-window-decorator
%endif
