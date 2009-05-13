Summary:	Install Debian and Slackware Packages with RPM
Name:		alien
Version:	8.75
Release:	%mkrel 1
URL:		http://kitenet.net/programs/code/alien
Source:		http://ftp.debian.org/debian/pool/main/a/alien/alien_%version.tar.gz
Patch0:		alien_8.74-do-not-own-sys-directories.diff
License:	GPLv2+
Group:		Archiving/Other
Buildroot:	%_tmppath/%name-buildroot
Requires:	perl, dpkg
BuildRequires:	perl-devel
BuildArch: noarch

%description
Alien is a program that converts between the rpm (Mandriva, Redhat ), 
dpkg (Debian), slp (Stampede), and tgz (Slackware) file formats. 
If you want to use a package from another distribution than the one 
you have installed on your system, you can use alien to convert 
it to your preferred package format and install it.

%prep
%setup -q -n alien
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
perl -pi -e 's/: :\s*extra_/:: extra_/' Makefile

%make
chmod 644 $RPM_BUILD_DIR/alien/patches/j2sdk*

%install
%makeinstall_std VARPREFIX=%buildroot PREFIX=%buildroot%_prefix


%files 
%defattr(-,root,root)
%_bindir/*
%dir %_datadir/alien
%_mandir/*/*
%{_datadir}/alien/patches
%{perl_vendorlib}/Alien
/var/lib/alien

%clean
rm -rf $RPM_BUILD_ROOT


