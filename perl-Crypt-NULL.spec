%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	NULL
Summary:	Crypt::NULL Perl module - NULL Encryption alghorithm
Summary(pl):	Modu³ Perla Crypt::NULL - algorytm szyfrowania NULL
Name:		perl-Crypt-NULL
Version:	1.02
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The NULL Encryption Algorithm is a symmetric block cipher described in
RFC 2410 by Rob Glenn and Stephen Kent. This module implements NULL
encryption. It supports the Crypt::CBC interface.

%description -l pl
Algorytm kodowania NULL jest symetrycznym szyfrem blokowym opisanym w
RFC 2410 przez Roba Glenna i Stephena Kenta. Ten modu³ jest
implementacj± kodowania NULL. Obs³uguje interfejs Crypt::CBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
%{perl_sitelib}/Crypt/NULL.pm
%{_mandir}/man3/*
