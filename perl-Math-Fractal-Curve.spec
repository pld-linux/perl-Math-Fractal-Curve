#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Fractal-Curve
Summary:	Math::Fractal::Curve - generate fractal curves
Summary(pl):	Math::Fractal::Curve - generowanie krzywych fraktalnych
Name:		perl-Math-Fractal-Curve
Version:	1.01
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	afd6e735b32ad634d8958b6c2dd30b2d
%if %{with tests}
BuildRequires:	perl(Test::More)
%endif
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended to generate 2-dimensional fractal curves such
as the von Koch curve from simple generator functions.

The fractals are generated by recursively replacing a distance with
the generator. Hence, the starting distance and the generator define
such a fractal curve. Generators describe what a given distance is
going to be replaced with in terms of lengths of the distance. For
example, a generator of ([0, 0, 1/3, 0], [2/3, 0, 1, 0]) describes a
Mid-third Cantor Set which means the the middle third of every
distance in the set is deleted. Syntax for generator data structures
in the context of this module is [[x1, y1, x2, y2], [X1, Y1, X2, Y2]]
(array ref of array refs of edge coordinates) where xn,yn are the two
coordinate pairs specifying the first edge a distance is to be
replaced with and Xn,Yn are the second edge. There may be any number
of edges.

%description -l pl
Ten modu� s�u�y do generowania 2-wymiarowych krzywych fraktalnych
takich jak krzywa von Kocha z prostszych funkcji generuj�cych.

Fraktale s� generowane przez rekurencyjne zast�powanie odcinka
generatorem. W ten spos�b pocz�tkowy odcinek i generator definiuj�
tak� krzyw� fraktaln�. Generatory opisuj�, czym zostanie zast�piony
dany odcinek w zale�no�ci od d�ugo�ci odcinka. Na przyk�ad generator
([0, 0, 1/3, 0], [2/3, 0, 1, 0]) opisuje zbi�r Kantora (ze �rodkow�
trzeci� cz�ci�) i oznacza, �e �rodkowa trzecia cz�� ka�dego
odcinka ze zbioru jest usuwana. Sk�adnia struktur danych generatora
w kontek�cie tego modu�u to [[x1, y1, x2, y2], [X1, Y1, X2, Y2]]
(referencja do tablicy referencji do wsp�rz�dnych ko�ca), gdzie
xn,yn to pary wsp�rz�dnych okre�laj�cych pierwszy koniec odcinka do
zast�pienia, a Xn,Yn to drugi koniec. Mo�e by� dowolna liczba ko�c�w.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/Fractal/Curve.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
