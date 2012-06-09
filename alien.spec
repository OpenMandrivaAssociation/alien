Summary:	Install Debian and Slackware Packages with RPM
Name:		alien
Version:	8.87
Release:	1
URL:		http://sourceforge.net/projects/alien/
Source:		http://ftp.debian.org/debian/pool/main/a/alien/%{name}_%version.tar.gz
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
%setup -q -n %{name}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
perl -pi -e 's/: :\s*extra_/:: extra_/' Makefile

%make

%install
%makeinstall_std VARPREFIX=%buildroot PREFIX=%buildroot%_prefix

%files 
%defattr(-,root,root)
%_bindir/*
%dir %_datadir/alien
%_mandir/*/*
%{_datadir}/alien/patches
/var/lib/alien
%doc README TODO

%files -n perl-Alien
%{perl_vendorlib}/Alien
%doc README TODO
