%define upstream_name    Catalyst-Plugin-PageCache
%define upstream_version 0.31

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Cache the output of entire pages
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Cache::Cache)
BuildRequires: perl(Cache::FileCache)
BuildRequires: perl(Catalyst::Plugin::Cache)
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(Digest::SHA1)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Path)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Many dynamic websites perform heavy processing on most pages, yet this
information may rarely change from request to request. Using the PageCache
plugin, you can cache the full output of different pages so they are served
to your visitors as fast as possible. This method of caching is very useful
for withstanding a Slashdotting, for example.

This plugin requires that you also load a Cache plugin. Please see the
Known Issues when choosing a cache backend.

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
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


