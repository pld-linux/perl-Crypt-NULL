%define		pdir	Crypt
%define		pnam	NULL
Summary:	Crypt::NULL Perl module - NULL encryption alghorithm
Summary(pl.UTF-8):	Moduł Perla Crypt::NULL - algorytm szyfrowania NULL
Name:		perl-Crypt-NULL
Version:	1.02
Release:	5
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	86918bc7d084be0600a26279304ed395
URL:		http://search.cpan.org/dist/Crypt-NULL/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The NULL Encryption Algorithm is a symmetric block cipher described in
RFC 2410 by Rob Glenn and Stephen Kent. This module implements NULL
encryption. It supports the Crypt::CBC interface.

%description -l pl.UTF-8
Algorytm kodowania NULL jest symetrycznym szyfrem blokowym opisanym w
RFC 2410 przez Roba Glenna i Stephena Kenta. Ten moduł jest
implementacją kodowania NULL. Obsługuje interfejs Crypt::CBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/NULL.pm
%{_mandir}/man3/*
