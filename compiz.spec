#
# TODO:
# - separate gnome control-panel plugin (it doesn't seem to work anyway)
#
Summary:	OpenGL window and compositing manager
Summary(pl):	OpenGL-owy zarz±dca okien i sk³adania
Name:		compiz
Version:	0.0.3
Release:	2
License:	GPL/MIT
Group:		X11
%define		_snap	20060222
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	054cfcedab9282f66e5ab89edbd49c35
Patch0:		%{name}-wobbly.patch
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	avahi-glib-devel
BuildRequires:	control-center-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-menus-devel
BuildRequires:	libsvg-cairo-devel
BuildRequires:	libwnck-devel
BuildRequires:	qt4-build
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

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p0

%build
autoreconf -v --install

%configure \
	--enable-svg \
	--enable-libsvg-cairo \
	--enable-gnome \
	--enable-kde

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/compiz
%attr(755,root,root) %{_libdir}/compiz/*.so
%attr(755,root,root) %{_libdir}/window-manager-settings/*.so
%{_datadir}/compiz
%{_datadir}/gnome/wm-properties/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/compiz
%{_pkgconfigdir}/*
