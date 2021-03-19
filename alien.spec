Summary:	Install Debian and Slackware Packages with RPM
Name:		alien
Version:	8.95.3
Release:	1
URL:		http://kitenet.net/~joey/code/alien/
Source0:	http://ftp.debian.org/debian/pool/main/a/alien/%{name}_%{version}.tar.xz
License:	GPLv2+
Group:		Archiving/Other
Requires:	perl, dpkg >= 1.13.26, rpm-build
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Alien is a program that converts between the rpm (Mandriva, Redhat ), 
dpkg (Debian), slp (Stampede), and tgz (Slackware) file formats. 
If you want to use a package from another distribution than the one 
you have installed on your system, you can use alien to convert 
it to your preferred package format and install it.

%package -n perl-Alien
Summary:        Alien Perl modules
Requires:	perl-base

%description -n perl-Alien
Alien is a program that converts between the rpm (Mandriva, Redhat ),
dpkg (Debian), slp (Stampede), and tgz (Slackware) file formats.
If you want to use a package from another distribution than the one
you have installed on your system, you can use alien to convert
it to your preferred package format and install it.

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
perl -pi -e 's/: :\s*extra_/:: extra_/' Makefile

%make_build

%install
%make_install VARPREFIX=%buildroot PREFIX=%buildroot%_prefix

%files 
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/Alien

%doc README TODO

%files -n perl-Alien
%{perl_vendorlib}/Alien
%doc README TODO


%changelog
* Sat Jun 09 2012 Bernhard Rosenkraenzer <bero@bero.eu> 8.87-1
+ Revision: 803858
- Fix unresolvable dependency in perl-Alien (versioned perl-base w/o epoch)
- Update to 8.87

* Sun Jan 29 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 8.86-1
+ Revision: 769588
- new version 8.86

* Wed Apr 27 2011 Leonardo Coelho <leonardoc@mandriva.org> 8.84-1
+ Revision: 659672
- new version

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 8.79-3mdv2011.0
+ Revision: 609966
- rebuild

* Wed Apr 21 2010 Sandro Cazzaniga <kharec@mandriva.org> 8.79-2mdv2010.1
+ Revision: 537465
- Fix URL
- replace %%clean section
- clean  in the beginning of %%install

* Sun Dec 27 2009 Thierry Vignaud <tv@mandriva.org> 8.79-1mdv2010.1
+ Revision: 482657
- new release
- requires rpm-build
- require a dpkg recent enough to support data.tar.lzma

* Thu Jul 09 2009 Frederik Himpe <fhimpe@mandriva.org> 8.78-1mdv2010.0
+ Revision: 394019
- update to new version 8.78

* Tue Jun 09 2009 Frederik Himpe <fhimpe@mandriva.org> 8.76-1mdv2010.0
+ Revision: 384469
- update to new version 8.76

* Wed May 13 2009 Thierry Vignaud <tv@mandriva.org> 8.75-1mdv2010.0
+ Revision: 375472
- new release
- patch 0: prevent owning system directories (such as /, /usr, /usr/lib, ...)

* Tue May 05 2009 Thierry Vignaud <tv@mandriva.org> 8.74-1mdv2010.0
+ Revision: 372142
- new release

  + Emmanuel Andry <eandry@mandriva.org>
    - New version
    - fix license

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 8.64-3mdv2009.0
+ Revision: 240427
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Mon Nov 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 8.64-1mdv2007.0
+ Revision: 77021
- Import alien

* Mon Nov 06 2006 Götz Waschk <waschk@mandriva.org> 8.64-1mdv2007.1
- new version

