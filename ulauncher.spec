Summary:	Linux Application Launcher
Name:		ulauncher
Version:	5.8.0
Release:	3
License:	GPL v3+
Group:		X11/Applications
Source0:	https://github.com/Ulauncher/Ulauncher/releases/download/%{version}/%{name}_%{version}.tar.gz
# Source0-md5:	49599615189481e06973e1c59fc9ff5c
URL:		https://ulauncher.io
BuildRequires:	python3-distutils-extra
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	gdk-pixbuf2
Requires:	glib2
Requires:	gtk+3
Requires:	gtk-webkit4
Requires:	keybinder3
Requires:	libappindicator-gtk3
Requires:	libnotify
Requires:	python3-Levenshtein
Requires:	python3-dbus
Requires:	python3-pyinotify
Requires:	python3-pyxdg
Requires:	python3-websocket-client
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ulauncher is a fast application launcher for Linux. It's is written in
Python, using GTK+.

%prep
%setup -q -n %{name}

# no py3_build: DistutilsExtra does not like being built twice
# and py3_install invokes build too

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/ulauncher

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/ulauncher
%attr(755,root,root) %{_bindir}/ulauncher-toggle
%{_datadir}/ulauncher
%{_desktopdir}/ulauncher.desktop
%{_iconsdir}/hicolor/scalable/apps/ulauncher.svg
%{_iconsdir}/hicolor/scalable/apps/ulauncher-indicator.svg
%{py3_sitescriptdir}/ulauncher
%{py3_sitescriptdir}/ulauncher-*-py*.egg-info
