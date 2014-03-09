%define debug_package %{nil}
%define __prefix /usr/local

Name:           kibana
Summary:        A browser based analytics and search interface to Logstash and other timestamped data sets stored in ElasticSearch
Version:        3.0.0milestone5
Release:        1%{?dist}
License:        Apache Software License 2.0
Group:          MAILRU
Prefix:         %{_prefix}

Url:            http://www.elasticsearch.org/overview/kibana/
Source0:        https://download.elasticsearch.org/kibana/kibana/%{name}-%{version}.zip
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
%{__cp} -r {app,css,font,img,vendor,config.js,index.html} %{buildroot}%{__prefix}/%{name}/
%{__cp} config.js %{buildroot}%{__prefix}/%{name}/config.default.js

%pre

%post

%preun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{__prefix}/%{name}/app
%{__prefix}/%{name}/css
%{__prefix}/%{name}/font
%{__prefix}/%{name}/img
%{__prefix}/%{name}/vendor
%{__prefix}/%{name}/config.default.js
%{__prefix}/%{name}/index.html
%config(noreplace) %{__prefix}/%{name}/config.js
