%define debug_package %{nil}
%define __jar_repack %{nil}
%define __os_install_post %{nil}
%define __prefix /usr/local

Name:           logstash
Summary:        A tool for managing events and logs
Version:        1.4.2
Release:        1%{?dist}
License:        Apache Software License 2.0
Group:          MAILRU
Prefix:         %{_prefix}

Url:            http://logstash.net
Source0:        https://download.elasticsearch.org/%{name}/%{name}/%{name}-%{version}.tar.gz
Source1:        https://download.elasticsearch.org/%{name}/%{name}/%{name}-contrib-%{version}.tar.gz
Source2:        logstash-logrotate.sh
Source3:        logstash-init.sh
Source4:        logstash-sysconfig.sh
Source5:        logstash-config.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

AutoReqProv:    no
Requires:       java-1.7.0-openjdk >= 1.7.0

Requires(post): chkconfig initscripts
Requires(pre):  chkconfig initscripts
Requires(pre):  shadow-utils

%description
A tool for managing events and logs

%prep
%setup -q -n %{name}-%{version}
gzip -dc %{SOURCE1} | tar -xf - --strip-components=1

%build
true

%install
rm -rf $RPM_BUILD_ROOT

%{__mkdir} -p %{buildroot}%{__prefix}/%{name}/
%{__cp} -r * %{buildroot}%{__prefix}/%{name}/

# Config
%{__mkdir} -p %{buildroot}%{_sysconfdir}/%{name}
%{__install} -m 755 %{SOURCE5} %{buildroot}%{_sysconfdir}/%{name}/logstash.conf

# Logs
%{__mkdir} -p %{buildroot}%{_localstatedir}/log/%{name}
%{__install} -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Misc
%{__mkdir} -p %{buildroot}%{_localstatedir}/run/%{name}

# sysconfig and init
%{__mkdir} -p %{buildroot}%{_initddir}
%{__mkdir} -p %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -m 755 %{SOURCE3} %{buildroot}%{_initddir}/%{name}
%{__install} -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

# Create Home directory
# See https://github.com/lfrancke/logstash-rpm/issues/5
%{__mkdir} -p %{buildroot}%{_sharedstatedir}/%{name}

%pre
# create logstash group
if ! getent group logstash >/dev/null; then
    groupadd -r logstash
fi

# create logstash user
if ! getent passwd logstash >/dev/null; then
    useradd -r -g logstash -d %{_sharedstatedir}/%{name} -s /sbin/nologin -c "Logstash service user" logstash
fi

%post
/sbin/chkconfig --add logstash

%preun
if [ $1 -eq 0 ]; then
    /sbin/service logstash stop >/dev/null 2>&1
    /sbin/chkconfig --del logstash
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{__prefix}/%{name}/
# Config
%config(noreplace) %{_sysconfdir}/%{name}/logstash.conf
# Logrotate
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
# Sysconfig and init
%{_initddir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/*
%defattr(-,%{name},%{name},-)
%dir %{_localstatedir}/log/%{name}/
%dir %{_localstatedir}/run/%{name}/
# Home directory
%dir %{_sharedstatedir}/%{name}/
