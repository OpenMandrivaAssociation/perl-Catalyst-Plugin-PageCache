%define upstream_name    Catalyst-Plugin-PageCache
%define upstream_version 0.31

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Cache the output of entire pages
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Cache::Cache)
BuildRequires:	perl(Cache::FileCache)
BuildRequires:	perl(Catalyst::Plugin::Cache)
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*




%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.310.0-2mdv2011.0
+ Revision: 656888
- rebuild for updated spec-helper

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.310.0-1mdv2011.0
+ Revision: 607794
- import perl-Catalyst-Plugin-PageCache

