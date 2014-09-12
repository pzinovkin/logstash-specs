%define debug_package %{nil}
%define __prefix /usr/local

Name:           kibana
Summary:        A browser based analytics and search interface to Logstash and other timestamped data sets stored in ElasticSearch
Version:        3.1.0
Release:        1%{?dist}
License:        Apache Software License 2.0
Group:          MAILRU
Prefix:         %{_prefix}

Url:            http://www.elasticsearch.org/overview/kibana/
Source0:        https://download.elasticsearch.org/%{name}/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A browser based analytics and search interface to Logstash and other timestamped data sets stored in ElasticSearch

%prep
%setup -q -n %{name}-%{version}

%build
true

%install
rm -rf $RPM_BUILD_ROOT

%{__mkdir} -p %{buildroot}%{__prefix}/%{name}/
%{__cp} -r * %{buildroot}%{__prefix}/%{name}/

%pre

%post

%preun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{__prefix}/%{name}/
%config(noreplace) %{__prefix}/%{name}/config.js
