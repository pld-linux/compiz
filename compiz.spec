#
# Conditional build:
%bcond_without	gnome		# don't build gnome-window-decorator
%bcond_with	kde		# build kde-window-decorator (currently not working)
#
Summary:	OpenGL window and compositing manager
Summary(pl):	OpenGL-owy zarz±dca okien i sk³adania
Name:		compiz
Version:	0.0.4
Release:	2
License:	GPL/MIT
Group:		X11
%define		_snap	20060301
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	2656d64e5046601d998227d401cc655f
Patch0:		%{name}-switcher-all-desktops.patch
BuildRequires:	GConf2-devel
BuildRequires:	OpenGL-devel
BuildRequires:	glib2-devel
BuildRequires:	libpng-devel
BuildRequires:	libsvg-cairo-devel
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-lib-libXcomposite
BuildRequires:	xorg-lib-libXdamage
BuildRequires:	xorg-lib-libXrandr
%if %{with gnome}
BuildRequires:	avahi-glib-devel
BuildRequires:	control-center-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-menus-devel
BuildRequires:	libwnck-devel
%endif
%if %{with kde}
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build
%endif
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
Requires:	%{name} = %{version}-%{release}

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

%build
autoreconf -v --install

%configure \
	--enable-svg \
	--enable-libsvg-cairo \
	--%{?with_gnome:en}%{!?with_gnome:dis}able-gnome \
	--%{?with_kde:en}%{!?with_kde:dis}able-kde

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/compiz
%dir %{_libdir}/compiz
%attr(755,root,root) %{_libdir}/compiz/*.so
%{_datadir}/compiz
%{_datadir}/gnome/wm-properties/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/compiz
%{_pkgconfigdir}/*

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
