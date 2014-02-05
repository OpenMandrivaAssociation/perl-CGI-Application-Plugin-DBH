%define upstream_name    CGI-Application-Plugin-DBH
%define upstream_version 4.04
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Easy DBI access from CGI::Application
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CGI/CGI-Application-Plugin-DBH-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI::Application)
BuildRequires:	perl(DBD::Mock)
BuildRequires:	perl(DBI)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::MockObject)

BuildArch:	noarch

%description
CGI::Application::Plugin::DBH adds easy access to a DBI database handle to
your CGI::Application modules. Lazy loading is used to prevent a database
connection from being made if the 'dbh' method is not called during the
request. In other words, the database connection is not created until it is
actually needed. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/CGI

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 4.0.0-2mdv2011.0
+ Revision: 680679
- mass rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 4.0.0-1mdv2011.0
+ Revision: 504596
- rebuild using %%perl_convert_version

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 4.00-2mdv2010.0
+ Revision: 440536
- rebuild

* Wed Nov 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.00-1mdv2009.1
+ Revision: 307068
- import perl-CGI-Application-Plugin-DBH


* Wed Nov 26 2008 cpan2dist 4.00-1mdv
- initial mdv release, generated with cpan2dist



