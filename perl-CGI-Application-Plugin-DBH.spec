%define upstream_name    CGI-Application-Plugin-DBH
%define upstream_version 4.00

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Easy DBI access from CGI::Application
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CGI::Application)
BuildRequires: perl(DBD::Mock)
BuildRequires: perl(DBI)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
CGI::Application::Plugin::DBH adds easy access to a DBI database handle to
your CGI::Application modules. Lazy loading is used to prevent a database
connection from being made if the 'dbh' method is not called during the
request. In other words, the database connection is not created until it is
actually needed. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/CGI
