Summary:	GNOME Iagno
Summary(pl.UTF-8):	Iagno dla GNOME
Name:		iagno
Version:	3.12.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/iagno/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	8363f71af8385f2855a2c46d3293a985
URL:		https://wiki.gnome.org/Apps/Iagno
BuildRequires:	appdata-tools
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	glib2 >= 1:2.36.0
Requires:	gtk+3 >= 3.10.0
Requires:	hicolor-icon-theme
Requires:	libcanberra-gtk3 >= 0.26
Requires:	librsvg >= 2.32.0
Provides:	gnome-games-iagno = 1:%{version}-%{release}
Obsoletes:	gnome-games-iagno < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reversi like game.

%description -l pl.UTF-8
Gra podobna do Reversi.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/iagno
%{_datadir}/appdata/iagno.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.iagno.gschema.xml
%{_datadir}/iagno
%{_desktopdir}/iagno.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_mandir}/man6/iagno.6*