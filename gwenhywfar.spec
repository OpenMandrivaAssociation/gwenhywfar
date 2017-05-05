%define major	60
%define libname	%mklibname %{name} %{major}

%define guimajor 0
%define libplugins %mklibname %{name}-plugins %{guimajor}
%define libgtkgui %mklibname gwengui-gtk2_ %{guimajor}
%define libqt4gui %mklibname gwengui-qt4_ %{guimajor}
%define cpplibname %mklibname gwengui-cpp %{guimajor}
%define devname %mklibname -d %{name}

Summary:	A multi-platform helper library for other libraries
Name:		gwenhywfar
Version:	4.17.0
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://gwenhywfar.sourceforge.net/
Source0:	http://files.hboeck.de/aq/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)

%description
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
and OpenHBCI-TNG (The Next Generation).

%package i18n
Summary:	A multi-platform helper library for other libraries - Translations
Group:		System/Internationalization
Conflicts:	%{name} < 4.3.3-2

%description i18n
This package contains the translations for %{name}.

%package tools
Summary:	A multi-platform helper library for other libraries - Tools
Group:		System/Libraries
Conflicts:	%{name} < 4.3.3-2
Conflicts:	%{_lib}gwenhywfar-devel < 4.3.3-2

%description tools
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
and OpenHBCI-TNG (The Next Generation).

%package -n %{libplugins}
Summary:	A multi-platform helper library for other libraries
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Requires:	%{name}-i18n >= %{version}-%{release}
Conflicts:	%{_lib}gwenhywfar60 < 4.3.3-2

%description -n %{libplugins}
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
and OpenHBCI-TNG (The Next Generation).

%package -n %{libname}
Summary:	A multi-platform helper library for other libraries
Group:		System/Libraries
Suggests:	%{libplugins} >= %{version}-%{release}

%description -n %{libname}
This package contains a shared library for %{name}.

%package -n %{libqt4gui}
Summary:	A multi-platform helper library for other libraries
Group:		System/Libraries

%description -n %{libqt4gui}
This package contains a shared library for %{name} - gui QT4.

%package -n %{libgtkgui}
Summary:	A multi-platform helper library for other libraries
Group:		System/Libraries

%description -n %{libgtkgui}
This package contains a shared library for %{name} - gui GTK+2.

%package -n %cpplibname
Summary: A multi-platform helper library for other libraries
Group: System/Libraries
Provides: %{name}-gui = %{version}

%description -n %cpplibname
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
and OpenHBCI-TNG (The Next Generation).

%package -n %{devname}
Summary:	Gwenhywfar development kit
Group:		Development/C
Requires:	%{libplugins} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libqt4gui} = %{version}-%{release}
Requires:	%{libgtkgui} = %{version}-%{release}
Requires:	%{cpplibname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains gwenhywfar-config and header files for writing and
compiling programs using Gwenhywfar.

%prep
%setup -q
%apply_patches

%build
%configure \
	--with-guis="qt4 gtk2" \
	--with-qt4-libs=%{qt4lib} \
	--enable-ssl \
	--with-openssl-libs=%{_libdir}
%make

%install
%makeinstall_std
%find_lang %{name}

ln -snf %{_sysconfdir}/pki/tls/certs/ca-bundle.crt %{buildroot}%{_datadir}/%{name}/ca-bundle.crt

%files i18n -f %{name}.lang

%files tools
%doc AUTHORS README
%{_bindir}/gct-tool
%{_bindir}/gsa
%{_bindir}/mklistdoc
%{_bindir}/typemaker
%{_bindir}/typemaker2
%{_bindir}/xmlmerge
%{_datadir}/%{name}

%files -n %{libplugins}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/%{major}
%dir %{_libdir}/%{name}/plugins/%{major}/configmgr
%dir %{_libdir}/%{name}/plugins/%{major}/ct
%dir %{_libdir}/%{name}/plugins/%{major}/dbio
%{_libdir}/%{name}/plugins/%{major}/configmgr/dir.so
%{_libdir}/%{name}/plugins/%{major}/configmgr/dir.xml
%{_libdir}/%{name}/plugins/%{major}/ct/ohbci.so
%{_libdir}/%{name}/plugins/%{major}/ct/ohbci.xml
%{_libdir}/%{name}/plugins/%{major}/dbio/*.so.%{guimajor}*
%{_libdir}/%{name}/plugins/%{major}/dbio/*.xml

%files -n %{libname}
%{_libdir}/libgwenhywfar.so.%{major}*

%files -n %{libqt4gui}
%{_libdir}/libgwengui-qt4.so.%{guimajor}*

%files -n %{libgtkgui}
%{_libdir}/libgwengui-gtk2.so.%{guimajor}*

%files -n %cpplibname
%{_libdir}/libgwengui-cpp.so.%{guimajor}
%{_libdir}/libgwengui-cpp.so.%{guimajor}.*

%files -n %{devname}
%{_bindir}/gwenhywfar-config
%{_includedir}/gwenhywfar4
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}/plugins/%{major}/dbio/*.so
%{_datadir}/aclocal/gwenhywfar.m4
%{_libdir}/cmake/*
