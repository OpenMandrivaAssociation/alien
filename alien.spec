Summary:	Install Debian and Slackware Packages with RPM
Name:		alien
Version:	8.79
Release:	%mkrel 2
URL:		http://sourceforge.net/projects/alien/
Source:		http://ftp.debian.org/debian/pool/main/a/alien/alien_%version.tar.gz
Patch0:		alien_8.74-do-not-own-sys-directories.diff
License:	GPLv2+
Group:		Archiving/Other
Buildroot:	%_tmppath/%name-buildroot
Requires:	perl, dpkg >= 1.13.26, rpm-build
BuildRequires:	perl-devel
BuildArch: noarch

%description
Alien is a program that converts between the rpm (Mandriva, Redhat ), 
dpkg (Debian), slp (Stampede), and tgz (Slackware) file formats. 
If you want to use a package from another distribution than the one 
you have installed on your system, you can use alien to convert 
it to your preferred package format and install it.

%prep
%setup -q -n %name
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
perl -pi -e 's/: :\s*extra_/:: extra_/' Makefile

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std VARPREFIX=%buildroot PREFIX=%buildroot%_prefix

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%_bindir/*
%dir %_datadir/alien
%_mandir/*/*
%{_datadir}/alien/patches
%{perl_vendorlib}/Alien
/var/lib/alien

