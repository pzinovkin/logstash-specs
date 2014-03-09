%define debug_package %{nil}
%define __prefix /usr/local

Name:           elasticsearch
Summary:        A distributed, highly available, RESTful search engine
Version:        0.90.9
Release:        1%{?dist}
License:        Apache Software License 2.0
Group:          MAILRU
Prefix:         %{_prefix}

Url:            http://www.elasticsearch.com
Source0:        http://download.elasticsearch.org/%{name}/%{name}/%{name}-%{version}.tar.gz
Source1:        elasticsearch-init.d
Source2:        elasticsearch-logrotate.d
Source3:        elasticsearch-config-logging.yml
Source4:        elasticsearch-sysconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       jpackage-utils
Requires:       jre >= 1.6.0

Requires(post): chkconfig initscripts
Requires(pre):  chkconfig initscripts
Requires(pre):  shadow-utils

%description
A distributed, highly available, RESTful search engine

%prep
%setup -q -n %{name}-%{version}

%build
true

%install
rm -rf $RPM_BUILD_ROOT

%{__mkdir} -p %{buildroot}%{__prefix}/%{name}/bin
%{__install} -p -m 755 bin/elasticsearch %{buildroot}%{__prefix}/%{name}/bin
%{__install} -p -m 644 bin/elasticsearch.in.sh %{buildroot}%{__prefix}/%{name}/bin
%{__install} -p -m 755 bin/plugin %{buildroot}%{__prefix}/%{name}/bin

#libs
%{__mkdir} -p %{buildroot}%{__prefix}/%{name}/lib/sigar
%{__install} -p -m 644 lib/*.jar %{buildroot}%{__prefix}/%{name}/lib
%{__install} -p -m 644 lib/sigar/*.jar %{buildroot}%{__prefix}/%{name}/lib/sigar
%{__install} -p -m 644 lib/sigar/libsigar-amd64-linux.so %{buildroot}%{__prefix}/%{name}/lib/sigar

# config
%{__mkdir} -p %{buildroot}%{_sysconfdir}/elasticsearch
%{__install} -m 644 config/elasticsearch.yml %{buildroot}%{_sysconfdir}/%{name}
%{__install} -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}/logging.yml

# data
%{__mkdir} -p %{buildroot}%{_localstatedir}/lib/%{name}

# logs
%{__mkdir} -p %{buildroot}%{_localstatedir}/log/%{name}
%{__install} -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/elasticsearch

# plugins
%{__mkdir} -p %{buildroot}%{__prefix}/%{name}/plugins

# sysconfig and init
%{__mkdir} -p %{buildroot}%{_sysconfdir}/rc.d/init.d
%{__mkdir} -p %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/rc.d/init.d/elasticsearch
%{__install} -m 755 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/elasticsearch

%{__mkdir} -p %{buildroot}%{_localstatedir}/run/elasticsearch
%{__mkdir} -p %{buildroot}%{_localstatedir}/lock/subsys/elasticsearch

%pre
# create elasticsearch group
if ! getent group elasticsearch >/dev/null; then
    groupadd -r elasticsearch
fi

# create elasticsearch user
if ! getent passwd elasticsearch >/dev/null; then
    useradd -r -g elasticsearch -d %{__prefix}/%{name} -s /sbin/nologin -c "You know, for search" elasticsearch
fi

%post
/sbin/chkconfig --add elasticsearch

%preun
if [ $1 -eq 0 ]; then
  	/sbin/service elasticsearch stop >/dev/null 2>&1
  	/sbin/chkconfig --del elasticsearch
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sysconfdir}/rc.d/init.d/elasticsearch
%config(noreplace) %{_sysconfdir}/sysconfig/elasticsearch
%{_sysconfdir}/logrotate.d/elasticsearch
%dir %{__prefix}/elasticsearch
%{__prefix}/elasticsearch/bin/*
%{__prefix}/elasticsearch/lib/*
%dir %{__prefix}/elasticsearch/plugins
%config(noreplace) %{_sysconfdir}/elasticsearch
%doc LICENSE.txt  NOTICE.txt  README.textile
%defattr(-,elasticsearch,elasticsearch,-)
%dir %{_localstatedir}/lib/elasticsearch
%{_localstatedir}/run/elasticsearch
%dir %{_localstatedir}/log/elasticsearch
