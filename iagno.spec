Summary:	GNOME Iagno - disk flipping game derived from Reversi
Summary(pl.UTF-8):	Iagno dla GNOME - gra w obracanie krążków wywodząca się z Reversi
Name:		iagno
Version:	3.36.3
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/iagno/3.36/%{name}-%{version}.tar.xz
# Source0-md5:	1393b9d499975041a9a3e1779816078d
URL:		https://wiki.gnome.org/Apps/Iagno
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.42.0
BuildRequires:	gsound-devel >= 1.0.2
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	librsvg-devel >= 1:2.32.0
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.27.1
BuildRequires:	vala-gsound >= 1.0.2
BuildRequires:	vala-librsvg >= 1:2.32.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.42.0
Requires:	glib2 >= 1:2.42.0
Requires:	gsound >= 1.0.2
Requires:	gtk+3 >= 3.24.0
Requires:	hicolor-icon-theme
Requires:	librsvg >= 1:2.32.0
Provides:	gnome-games-iagno = 1:%{version}-%{release}
Obsoletes:	gnome-games-iagno < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Iagno is a Reversi like game.

%description -l pl.UTF-8
GNOME Iagno to gra podobna do Reversi.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%doc COPYING.images NEWS README.md
%attr(755,root,root) %{_bindir}/iagno
%{_datadir}/dbus-1/services/org.gnome.Reversi.service
%{_datadir}/glib-2.0/schemas/org.gnome.Reversi.gschema.xml
%{_datadir}/iagno
%{_datadir}/metainfo/org.gnome.Reversi.appdata.xml
%{_desktopdir}/org.gnome.Reversi.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Reversi.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Reversi-symbolic.svg
%{_mandir}/man6/iagno.6*
