%define name gwenhywfar
%define major 60
%define libname %mklibname %{name} %{major}
%define qt4major 0
%define gtkmajor 0
%define gtklibname %mklibname gwengui-gtk2_ %{gtkmajor}
%define qt4libname %mklibname gwengui-qt4_ %{qt4major}
%define develname %mklibname -d %{name}

Summary:	A multi-platform helper library for other libraries
Name:		gwenhywfar
Version:	4.3.3
Release:	1
Group:		System/Libraries
License:	LGPLv2+
URL:		http://gwenhywfar.sourceforge.net/
# http://www2.aquamaniac.de/sites/download/packages.php
Source0:	http://files.hboeck.de/aq/%{name}-%{version}.tar.gz
BuildRequires:	automake
BuildRequires:	autoconf >= 2.58
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	zlib-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(gtk+-2.0)
Suggests:	%{name}-gui = %{version}

%description
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
and OpenHBCI-TNG (The Next Generation).

%package -n %{libname}
Summary:	A multi-platform helper library for other libraries
Group:		System/Libraries
Requires:	%{name} >= %{version}

%description -n %{libname}
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
and OpenHBCI-TNG (The Next Generation).

%package -n %{qt4libname}
Summary:	A multi-platform helper library for other libraries
Group:		System/Libraries
Provides:	%{name}-gui = %{version}

%description -n %{qt4libname}
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
and OpenHBCI-TNG (The Next Generation).

%package -n %{gtklibname}
Summary:	A multi-platform helper library for other libraries
Group:		System/Libraries
Provides:	%{name}-gui = %{version}

%description -n %{gtklibname}
This is Gwenhywfar, a multi-platform helper library for networking and
security applications and libraries. It is heavily used by libchipcard
and OpenHBCI-TNG (The Next Generation).

%package -n %{develname}
Summary:	Gwenhywfar development kit
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{qt4libname} = %{version}-%{release}
Requires:	%{gtklibname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains gwenhywfar-config and header files for writing and
compiling programs using Gwenhywfar.

%prep
%setup -q

%build
%configure2_5x --disable-static \
  --disable-rpath \
  --with-guis="qt4 gtk2" --with-qt4-libs=%{qt4lib} \
  --with-openssl-libs=%{_libdir}
%make

%install
rm -fr %{buildroot} %{name}.lang
%makeinstall_std

%find_lang %{name}
perl -pi -e "s#-L%{_builddir}/%{name}-%{version}/src##" %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/%{name}/plugins/*/*/*.la
ln -snf %{_sysconfdir}/pki/tls/certs/ca-bundle.crt %{buildroot}%{_datadir}/%{name}/ca-bundle.crt

%files -f %{name}.lang
%doc AUTHORS README
%{_bindir}/gct-tool
%{_datadir}/%{name}

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*
%{_libdir}/%{name}

%files -n %{qt4libname}
%{_libdir}/libgwengui-qt4.so.%{qt4major}
%{_libdir}/libgwengui-qt4.so.%{qt4major}.*

%files -n %{gtklibname}
%{_libdir}/libgwengui-gtk2.so.%{gtkmajor}
%{_libdir}/libgwengui-gtk2.so.%{gtkmajor}.*

%files -n %{develname}
%{_bindir}/gwenhywfar-config
%{_bindir}/gsa
%{_bindir}/xmlmerge
%{_bindir}/mklistdoc
%{_bindir}/typemaker
%{_bindir}/typemaker2
%{_includedir}/gwenhywfar4
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/gwenhywfar.m4

%changelog
* Mon Mar 26 2012 Bernhard Rosenkraenzer <bero@bero.eu> 4.3.2-1
+ Revision: 787039
- Build for gnutls 3.x
- 4.3.2

* Fri Jan 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 4.3.1-1
+ Revision: 758294
- version update 4.3.1

* Tue Sep 27 2011 Andrey Bondrov <abondrov@mandriva.org> 4.3.0-1
+ Revision: 701422
- New version: 4.3.0

* Thu Aug 25 2011 Götz Waschk <waschk@mandriva.org> 4.2.1-1
+ Revision: 696556
- new version
- update file lists

* Mon Jun 20 2011 Oden Eriksson <oeriksson@mandriva.com> 4.1.0-2
+ Revision: 686312
- avoid pulling 32 bit libraries on 64 bit arch

* Tue Jun 14 2011 Funda Wang <fwang@mandriva.org> 4.1.0-1
+ Revision: 685095
- new version 4.1.0

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 4.0.9-1
+ Revision: 680642
- new verison 4.0.9

* Fri Apr 08 2011 Oden Eriksson <oeriksson@mandriva.com> 4.0.7-3
+ Revision: 651889
- force the usage of rootcerts and the up to date common ca-bundle.crt

* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 4.0.7-2
+ Revision: 639992
- rebuild

* Tue Feb 22 2011 Götz Waschk <waschk@mandriva.org> 4.0.7-1
+ Revision: 639281
- new version
-fix URL

* Wed Feb 16 2011 Götz Waschk <waschk@mandriva.org> 4.0.5-1
+ Revision: 638019
- new version

* Wed Feb 09 2011 Funda Wang <fwang@mandriva.org> 4.0.4-1
+ Revision: 636962
- 4.0.4

* Tue Nov 23 2010 Funda Wang <fwang@mandriva.org> 4.0.2-1mdv2011.0
+ Revision: 599869
- new version 4.0.2

* Tue Sep 21 2010 Funda Wang <fwang@mandriva.org> 4.0.1-1mdv2011.0
+ Revision: 580313
- new version 4.0.1
- promote gui package for downstream programs

* Mon Aug 30 2010 Funda Wang <fwang@mandriva.org> 4.0.0-1mdv2011.0
+ Revision: 574498
- new version 4.0.0

* Mon Aug 30 2010 Funda Wang <fwang@mandriva.org> 3.99.25-1mdv2011.0
+ Revision: 574282
- new version 3.99.25

* Sat Aug 21 2010 Funda Wang <fwang@mandriva.org> 3.99.22-1mdv2011.0
+ Revision: 571749
- New version 3.99.22

* Wed Aug 04 2010 Funda Wang <fwang@mandriva.org> 3.99.16-1mdv2011.0
+ Revision: 565947
- New version 3.99.16

* Thu Jul 29 2010 Funda Wang <fwang@mandriva.org> 3.99.13-1mdv2011.0
+ Revision: 562952
- 3.99.13 towards 4.0

* Fri May 07 2010 Funda Wang <fwang@mandriva.org> 3.11.7-3mdv2010.1
+ Revision: 543198
- rebuild

* Sun May 02 2010 Funda Wang <fwang@mandriva.org> 3.11.7-2mdv2010.1
+ Revision: 541604
- fix obsoletes

* Wed Apr 14 2010 Funda Wang <fwang@mandriva.org> 3.11.7-1mdv2010.1
+ Revision: 534692
- new version 3.11.7

* Tue Apr 06 2010 Funda Wang <fwang@mandriva.org> 3.11.6-3mdv2010.1
+ Revision: 532083
- rebuild for new openssl

* Wed Mar 31 2010 Funda Wang <fwang@mandriva.org> 3.11.6-2mdv2010.1
+ Revision: 530479
- fix wrong pkg name

* Wed Mar 31 2010 Funda Wang <fwang@mandriva.org> 3.11.6-1mdv2010.1
+ Revision: 530459
- New version 3.11.6

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 3.11.3-2mdv2010.1
+ Revision: 511572
- rebuilt against openssl-0.9.8m

* Sat Jan 02 2010 Frederik Himpe <fhimpe@mandriva.org> 3.11.3-1mdv2010.1
+ Revision: 485006
- Update to new version 3.11.3

* Tue Oct 06 2009 Thierry Vignaud <tv@mandriva.org> 3.11.1-2mdv2010.0
+ Revision: 454745
- do not package huge ChangeLog

* Wed Sep 23 2009 Frederik Himpe <fhimpe@mandriva.org> 3.11.1-1mdv2010.0
+ Revision: 448014
- Update to new version 3.11.1

* Fri Sep 11 2009 Emmanuel Andry <eandry@mandriva.org> 3.10.1-1mdv2010.0
+ Revision: 438475
- New version 3.10.1

* Sun Jun 21 2009 Funda Wang <fwang@mandriva.org> 3.9.0-1mdv2010.0
+ Revision: 387555
- new version 2.9.0

* Sat Jun 06 2009 Götz Waschk <waschk@mandriva.org> 3.8.2-1mdv2010.0
+ Revision: 383345
- new version
- drop patch 1

* Sat May 30 2009 Funda Wang <fwang@mandriva.org> 3.8.1-1mdv2010.0
+ Revision: 381420
- fix build with gnutls 2.8
- New version 3.8.1

* Tue Apr 28 2009 Götz Waschk <waschk@mandriva.org> 3.8.0-1mdv2010.0
+ Revision: 369098
- new version
- drop patch 1
- update URL

* Wed Mar 04 2009 Götz Waschk <waschk@mandriva.org> 3.7.2-1mdv2009.1
+ Revision: 348225
- update to new version 3.7.2

* Sat Jan 31 2009 Funda Wang <fwang@mandriva.org> 3.7.1-1mdv2009.1
+ Revision: 335855
- New version 3.7.1

* Fri Jan 23 2009 Funda Wang <fwang@mandriva.org> 3.7.0-1mdv2009.1
+ Revision: 332694
- New version 3.7.0

* Thu Dec 04 2008 Götz Waschk <waschk@mandriva.org> 3.5.2-2mdv2009.1
+ Revision: 309997
- rebuild to get rid of libtasn1 dep
- fix source URL

* Mon Nov 10 2008 Götz Waschk <waschk@mandriva.org> 3.5.2-1mdv2009.1
+ Revision: 301681
- new version

* Sat Oct 18 2008 Götz Waschk <waschk@mandriva.org> 3.5.1-1mdv2009.1
+ Revision: 294849
- new version

* Wed Aug 20 2008 Götz Waschk <waschk@mandriva.org> 3.4.1-1mdv2009.0
+ Revision: 274270
- update build deps
- new version
- update license
- fix build

* Wed Jul 09 2008 Götz Waschk <waschk@mandriva.org> 3.3.5-1mdv2009.0
+ Revision: 233016
- new version

* Sat Jun 14 2008 Funda Wang <fwang@mandriva.org> 3.3.4-1mdv2009.0
+ Revision: 219134
- New version 3.3.4

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 08 2008 Funda Wang <fwang@mandriva.org> 3.3.3-1mdv2009.0
+ Revision: 216783
- New version 3.3.3

* Wed May 28 2008 Funda Wang <fwang@mandriva.org> 3.3.2-2mdv2009.0
+ Revision: 212177
- New version 3.3.2

  + Götz Waschk <waschk@mandriva.org>
    - new version

* Tue Apr 22 2008 Götz Waschk <waschk@mandriva.org> 3.3.0-1mdv2009.0
+ Revision: 196639
- new version
- back to 3.2.0

  + mandrake <mandrake@mandriva.com>
    - %repsys markrelease
      version: 3.2.0
      release: 1mdv2009.0
      revision: 194557
      Copying 3.2.0-1mdv2009.0 to releases/ directory.

* Wed Apr 16 2008 Funda Wang <fwang@mandriva.org> 3.2.0-1mdv2009.0
+ Revision: 194557
- BR libgcrypt-devel
- New version 3.2.0
- New major 38->47

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - remove useless URLs of other projects from descriptions

* Fri Nov 23 2007 Götz Waschk <waschk@mandriva.org> 2.6.2-1mdv2008.1
+ Revision: 111451
- new version

* Wed Sep 05 2007 Götz Waschk <waschk@mandriva.org> 2.6.1-1mdv2008.0
+ Revision: 79972
- new version
- new devel name

* Sat May 19 2007 Götz Waschk <waschk@mandriva.org> 2.5.4-1mdv2008.0
+ Revision: 28457
- new version


* Thu Dec 28 2006 Götz Waschk <waschk@mandriva.org> 2.5.0-1mdv2007.0
+ Revision: 102209
- new version
- unpack patch

* Wed Sep 27 2006 Götz Waschk <waschk@mandriva.org> 2.4.1-1mdv2007.0
- New version 2.4.1

* Sun Aug 27 2006 Götz Waschk <waschk@mandriva.org> 2.4.0-1mdv2007.0
- New release 2.4.0

* Sat Jul 15 2006 Götz Waschk <waschk@mandriva.org> 2.3.1-1
- New release 2.3.1

* Sat Jun 17 2006 Götz Waschk <waschk@mandriva.org> 2.3.0-1mdv2007.0
- New release 2.3.0

* Fri Apr 14 2006 Götz Waschk <waschk@mandriva.org> 2.2.0-1mdk
- New release 2.2.0

* Tue Mar 28 2006 Götz Waschk <waschk@mandriva.org> 2.1.1-1mdk
- New release 2.1.1

* Tue Mar 21 2006 Götz Waschk <waschk@mandriva.org> 2.1.0-1mdk
- New release 2.1.0

* Tue Feb 28 2006 Götz Waschk <waschk@mandriva.org> 2.0.0-1mdk
- New release 2.0.0

* Tue Feb 07 2006 Götz Waschk <waschk@mandriva.org> 1.99.7-1mdk
- New release 1.99.7

* Tue Jan 31 2006 Götz Waschk <waschk@mandriva.org> 1.99.6-1mdk
- New release 1.99.6

* Thu Jan 26 2006 Götz Waschk <waschk@mandriva.org> 1.99.5-1mdk
- New release 1.99.5

* Wed Jan 18 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.99.4-1mdk
- New release 1.99.4

* Wed Jan 11 2006 G�tz Waschk <waschk@mandriva.org> 1.99.3-1mdk
- new major
- New release 1.99.3

* Thu Dec 15 2005 Götz Waschk <waschk@mandriva.org> 1.99.2-1mdk
- New release 1.99.2

* Thu Dec 08 2005 G�tz Waschk <waschk@mandriva.org> 1.99.1-2mdk
- fix deps for upgrades

* Fri Dec 02 2005 G�tz Waschk <waschk@mandriva.org> 1.99.1-1mdk
- new major
- update file list
- New release 1.99.1

* Thu Nov 17 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.19.0-2mdk
- rebuild against openssl-0.9.8
- add missing buildrequires

* Wed Nov 02 2005 G�tz Waschk <waschk@mandriva.org> 1.19.0-1mdk
- update file list
- New release 1.19.0

* Thu Aug 25 2005 Götz Waschk <waschk@mandriva.org> 1.17.0-1mdk
- New release 1.17.0

* Fri Aug 12 2005 G�tz Waschk <waschk@mandriva.org> 1.15.0-1mdk
- update file list
- New release 1.15.0

* Tue Jul 12 2005 G�tz Waschk <waschk@mandriva.org> 1.14.0-1mdk
- New release 1.14.0

* Wed Jun 15 2005 G�tz Waschk <waschk@mandriva.org> 1.13.3-1mdk
- New release 1.13.3

* Sat May 28 2005 G�tz Waschk <waschk@mandriva.org> 1.13.2-1mdk
- New release 1.13.2

* Thu May 26 2005 G�tz Waschk <waschk@mandriva.org> 1.13.1-1mdk
- New release 1.13.1

* Sat May 21 2005 G�tz Waschk <waschk@mandriva.org> 1.13.0-1mdk
- New release 1.13.0

* Tue May 03 2005 G�tz Waschk <waschk@mandriva.org> 1.12.1-1mdk
- New release 1.12.1

* Tue Apr 26 2005 G�tz Waschk <waschk@mandriva.org> 1.12.0-1mdk
- New release 1.12.0

* Thu Apr 07 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 1.10.0-1mdk 
- Release 1.10.0
- Regenerate patch0

* Tue Mar 08 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.8.0-2mdk
- lib64 fixes

* Mon Feb 21 2005 G�tz Waschk <waschk@linux-mandrake.com> 1.8.0-1mdk
- add CA Certificates file
- New release 1.8.0

* Tue Feb 15 2005 Jerome Soyer <saispo@mandrake.org> 1.7.2-1mdk
- New release

* Mon Dec 13 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.3-2mdk
- fix provides

* Mon Dec 13 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.3-1mdk
- initial package

