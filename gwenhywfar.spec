%define name gwenhywfar
%define major 47
%define libname %mklibname %name %major
%define qt4major 0
%define qt4libname %mklibname gwengui-qt4_ %{qt4major}
%define develname %mklibname -d %name

Summary: A multi-platform helper library for other libraries
Name: gwenhywfar
Version: 3.11.6
Release: %mkrel 3
#http://www2.aquamaniac.de/sites/download/download.php?package=01&release=23&file=01&dummy=gwenhywfar-3.8.2.tar.gz
Source: http://files.hboeck.de/aq/%{name}-%{version}beta.tar.gz
Patch2: gwenhywfar-3.11.6-fix-linkage.patch
BuildRequires: automake
BuildRequires: autoconf >= 2.58
BuildRequires: gettext-devel
BuildRequires: openssl-devel
BuildRequires: ncurses-devel
BuildRequires: zlib-devel
BuildRequires: libgcrypt-devel
BuildRequires: gnutls-devel
BuildRequires: qt4-devel
BuildConflicts: %{develname} < %{version}
Group: System/Libraries
License: LGPLv2+
URL: http://gwenhywfar.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
and OpenHBCI-TNG (The Next Generation).

%package -n %libname
Summary: A multi-platform helper library for other libraries
Group: System/Libraries
Requires: %name >= %version

%description -n %libname
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
and OpenHBCI-TNG (The Next Generation).

%package -n %qt4libname
Summary: A multi-platform helper library for other libraries
Group: System/Libraries
Obsoletes: %{_lib}gwengui-qt4_0}

%description -n %qt4libname
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
and OpenHBCI-TNG (The Next Generation).

%package -n %develname
Summary: Gwenhywfar development kit
Group: Development/C
Requires: %{libname} = %{version}
Requires: %{qt4libname} = %{version}
Provides: lib%name-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}
Obsoletes: %mklibname -d %name 38

%description -n %develname
This package contains gwenhywfar-config and header files for writing and
compiling programs using Gwenhywfar.

%prep
%setup -qn %name-%{version}beta
%patch2 -p0 -b .link

%build
%configure2_5x --disable-static \
  --disable-rpath \
  --with-guis=qt4 --with-qt4-libs=%{qt4lib} \
  --with-openssl-libs=%{_libdir}
%make

%install
rm -fr $RPM_BUILD_ROOT %name.lang
%makeinstall_std
find %buildroot -name \*.la|xargs chmod 644
%find_lang %name
perl -pi -e "s°-L$RPM_BUILD_DIR/%name-%version/src°°" %buildroot%_libdir/*.la %buildroot%_libdir/%name/plugins/*/*/*.la

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS README 
%_bindir/gct-tool
%_datadir/%name

%files -n %libname
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*
%{_libdir}/%{name}

%files -n %qt4libname
%defattr(-,root,root)
%{_libdir}/libgwengui-qt4.so.%{qt4major}
%{_libdir}/libgwengui-qt4.so.%{qt4major}.*

%files -n %develname
%defattr(-,root,root)
%{_bindir}/gwenhywfar-config
%{_bindir}/xmlmerge
%{_bindir}/mklistdoc
%{_bindir}/typemaker
%{_bindir}/typemaker2
%{_includedir}/gwenhywfar3
%{_includedir}/gwen-gui-qt4
%{_libdir}/*.so
%attr(644,root,root)  %{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/gwenhywfar.m4
