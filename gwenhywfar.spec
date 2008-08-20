%define name gwenhywfar
%define major 47
%define libname %mklibname %name %major
%define develname %mklibname -d %name
Summary: A multi-platform helper library for other libraries
Name: gwenhywfar
Version: 3.4.1
Release: %mkrel 1
Source: http://prdownloads.sourceforge.net/gwenhywfar/%{name}-%{version}.tar.gz
Patch0: gwenhywfar-1.10.0-lib64.patch
BuildRequires: automake
BuildRequires: autoconf >= 2.58
BuildRequires: openssl-devel
BuildRequires: ncurses-devel
BuildRequires: zlib-devel
BuildRequires: libgcrypt-devel
BuildRequires: gnutls-devel
Group: System/Libraries
License: LGPLv2+
URL: http://sourceforge.net/projects/gwenhywfar
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

%package -n %develname
Summary: Gwenhywfar development kit
Group: Development/C
Requires: %{libname} = %{version}
Provides: lib%name-devel = %{version}-%{release}
Obsoletes: %mklibname -d %name 38

%description -n %develname
This package contains gwenhywfar-config and header files for writing and
compiling programs using Gwenhywfar.

%prep
%setup -q
%patch0 -p1 -b .lib64
cp /usr/share/gettext/config.rpath .
make -f Makefile.cvs

%build
%configure2_5x --disable-static
%make LIBS=-lpthread

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
%doc AUTHORS README ChangeLog
%_bindir/gct-tool
%_datadir/%name

%files -n %libname
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*
%{_libdir}/%{name}

%files -n %develname
%defattr(-,root,root)
%{_bindir}/gwenhywfar-config
%{_bindir}/xmlmerge
%{_bindir}/mklistdoc
%{_bindir}/typemaker
%{_includedir}/gwenhywfar3
%{_libdir}/*.so
%attr(644,root,root)  %{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/gwenhywfar.m4
