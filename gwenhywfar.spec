%define major	79
%define libname	%mklibname %{name} %{major}

%define _disable_lto 1

%define guimajor %{major}
%define libplugins %mklibname %{name}-plugins %{guimajor}
%define libgtk3gui %mklibname gwengui-gtk3_ %{guimajor}
%define libqt6gui %mklibname gwengui-qt6_ %{guimajor}
%define cpplibname %mklibname gwengui-cpp %{guimajor}
%define devname %mklibname -d %{name}

Summary:	A multi-platform helper library for other libraries
Name:		gwenhywfar
Version:	5.14.1
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		https://www.aqbanking.de/
Source0:	https://www.aquamaniac.de/rdm/attachments/download/630/gwenhywfar-%{version}.tar.gz
# or git mirror https://github.com/aqbanking/gwenhywfar

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	pkgconfig(ice)
BuildRequires:	cmake
BuildRequires:	qmake-qt6
BuildRequires:	gettext-devel
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gtk+-3.0)
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

%package -n %{libqt6gui}
Summary:	A multi-platform helper library for other libraries
Group:		System/Libraries

%description -n %{libqt6gui}
This package contains a shared library for %{name} - gui QT6.

%package -n %{libgtk3gui}
Summary:        A multi-platform helper library for other libraries
Group:          System/Libraries

%description -n %{libgtk3gui}
This package contains a shared library for %{name} - gui GTK+3.

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
Requires:	%{libqt6gui} = %{version}-%{release}
Requires:	%{libgtk3gui} = %{version}-%{release}
Requires:	%{cpplibname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains gwenhywfar-config and header files for writing and
compiling programs using Gwenhywfar.

%prep
%autosetup -p1

autoreconf -fiv


%build

%ifarch %ix86
# cb - for some reason this doesnt get set on x86_32
export CXX="%__cxx -std=gnu++11"
%endif

export PATH=%_qt5_bindir:$PATH

%configure \
	--with-guis="qt5 gtk3" \
	--enable-ssl \
	--with-openssl-libs=%{_libdir} || (cat config.log && exit 1)

%make QT_LIBS='-lQt6Core -lQt6Gui -lQt6Widgets'

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
%{_libdir}/%{name}/plugins/%{major}/dbio/*.so.0*
%{_libdir}/%{name}/plugins/%{major}/dbio/*.xml

%files -n %{libname}
%{_libdir}/libgwenhywfar.so.%{major}*

%files -n %{libqt6gui}
%{_libdir}/libgwengui-qt5.so.%{guimajor}*

%files -n %{libgtk3gui}
%{_libdir}/libgwengui-gtk3.so.%{guimajor}*

%files -n %cpplibname
%{_libdir}/libgwengui-cpp.so.%{guimajor}
%{_libdir}/libgwengui-cpp.so.%{guimajor}.*

%files -n %{devname}
%{_bindir}/gwenhywfar-config
%{_includedir}/gwenhywfar5
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}/plugins/%{major}/dbio/*.so
%{_datadir}/aclocal/gwenhywfar.m4
%{_libdir}/cmake/*
