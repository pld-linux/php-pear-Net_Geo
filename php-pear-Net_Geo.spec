%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       Geo
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - geographical locations based on Internet address
Summary(pl):	%{_class}_%{_subclass} - po³o¿enie geograficzne na podstawie adresu internetowego
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Obtains geographical information based on IP number, domain name, or
AS number. Makes use of CAIDA Net_Geo lookup or locaizer extension.

%description -l pl
Uzyskuje informacje geograficzne, bazuj±c na numerach IP, nazwach
domen oraz numerów AS-ów. U¿ywa CAIDA Net_Geo lub rozszerzenia
locaizer.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/README
%{php_pear_dir}/%{_class}/*.php
