%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	Net_Geo
Summary:	%{_pearname} - geographical locations based on Internet address
Summary(pl.UTF-8):	%{_pearname} - położenie geograficzne na podstawie adresu internetowego
Name:		php-pear-%{_pearname}
Version:	1.0.5
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	49e1ebe6920e92624e234e34a1138c02
URL:		http://pear.php.net/package/Net_Geo/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Cache
Requires:	php-pear-PEAR-core
Requires:	php-pear-XML_Serializer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Obtains geographical information based on IP number, domain name, or
AS number. Makes use of CAIDA Net_Geo lookup or locaizer extension.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Uzyskuje informacje geograficzne, bazując na numerach IP, nazwach
domen oraz numerów AS-ów. Używa CAIDA Net_Geo lub rozszerzenia
locaizer.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/README
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/*.php
