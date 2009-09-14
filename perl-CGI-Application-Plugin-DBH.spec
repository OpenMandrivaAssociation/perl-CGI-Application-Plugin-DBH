%define module   CGI-Application-Plugin-DBH
%define version    4.00
%define release    %mkrel 2

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Easy DBI access from CGI::Application
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/CGI/%{module}-%{version}.tar.gz
BuildRequires: perl(CGI::Application)
BuildRequires: perl(DBD::Mock)
BuildRequires: perl(DBI)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
CGI::Application::Plugin::DBH adds easy access to a DBI database handle to
your CGI::Application modules. Lazy loading is used to prevent a database
connection from being made if the 'dbh' method is not called during the
request. In other words, the database connection is not created until it is
actually needed. 

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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

