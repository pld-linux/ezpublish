Summary:	eZ publish content management system
Summary(pl.UTF-8):	eZ publish - system zarządzania treścią
Name:		ezpublish
Version:	3.5.1
Release:	2
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.ez.no/content/download/80973/327487/file/%{name}-%{version}.tar.bz2
# Source0-md5:	e2a9c8b79edba287f2624fd3aa9259ae
URL:		http://ez.no/
Requires:	apache(mod_rewrite)
Requires:	php(gd)
Requires:	php(pcre)
Requires:	webserver = apache
Requires:	webserver(php)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eZ publish is an open source content management system and development
framework.

%description -l pl.UTF-8
eZ publish jest systemem zarządzania treścią z otwartym kodem
źródłowym.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

#chmod og+rwx -R var

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
