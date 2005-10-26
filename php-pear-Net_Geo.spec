%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Geo
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - geographical locations based on Internet address
Summary(pl):	%{_pearname} - po�o�enie geograficzne na podstawie adresu internetowego
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	30a0a736fae32e9dacf51528e4387fe6
URL:		http://pear.php.net/package/Net_Geo/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
Requires:	php-pear-Cache
Requires:	php-pear-PEAR
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Obtains geographical information based on IP number, domain name, or
AS number. Makes use of CAIDA Net_Geo lookup or locaizer extension.

In PEAR status of this package is: %{_status}.

%description -l pl
Uzyskuje informacje geograficzne, bazuj�c na numerach IP, nazwach
domen oraz numer�w AS-�w. U�ywa CAIDA Net_Geo lub rozszerzenia
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
%{php_pear_dir}/%{_class}/*.php
