Summary:	eZ publish content management system
Summary(pl):	eZ publish system zarz±dzania zawarto¶ci±
Name:		ezpublish
Version:	3.4.0
Release:	0.1
License:	GPL
Group:      Networking/Daemons
#Vendor:		-
#Icon:		-
Source0:	http://ez.no/content/download/59322/158350/file/%{name}-%{version}.tar.bz2
# Source0-md5:	3512cd5e1b9624c35e3ef56dcdf4fcbd
#Patch0:		%{name}-what.patch
URL:		http://ez.no
BuildRequires:	mysql-libs
#PreReq:		-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
#Requires:	mysql-libs
#Requires:	postgresql-libs
Requires:	apache
Requires:	apache-mod_rewrite
Requires:	php
Requires:	php-gd

#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eZ publish is an open source content management system and development
framework.

%description -l pl
eZ publish jest systemem zarz±dzania tre¶ci± z otwartym kodem ¼ród³owym.

#%package subpackage
#Summary:	-
#Summary(pl):	-
#Group:		-
#
#%description subpackage
#
#%description subpackage -l pl

%prep
%setup -q 
#-n %{name}-%{version}
#%patch0 -p1

#%build
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
#chown -R nouser.nouser var

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

#%files subpackage
#%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
