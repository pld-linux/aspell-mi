Summary:	Maori dictionary for aspell
Summary(pl.UTF-8):	Słownik maoryjski dla aspella
Name:		aspell-mi
Version:	0.50
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/mi/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	8b1a07032ee086662bfe44a2e0459db4
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Maori dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik maoryjski (lista słów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
