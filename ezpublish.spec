Summary:	eZ publish content management system
Summary(pl):	eZ publish - system zarz±dzania tre¶ci±
Name:		ezpublish
Version:	3.4.0
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://ez.no/content/download/59322/158350/file/%{name}-%{version}.tar.bz2
# Source0-md5:	3512cd5e1b9624c35e3ef56dcdf4fcbd
URL:		http://ez.no/
BuildRequires:	mysql-libs
Requires:	apache
Requires:	apache-mod_rewrite
Requires:	php
Requires:	php-gd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eZ publish is an open source content management system and development
framework.

%description -l pl
eZ publish jest systemem zarz±dzania tre¶ci± z otwartym kodem
¼ród³owym.

%prep
%setup -q 

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%{__gettextize}
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
%configure
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
