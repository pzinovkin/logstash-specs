Logstash SPECS for CentOS
=========================

All that you need to build CentOS RPMs for:

* [ElasticSearch][elasticsearch] 0.90.9
* [LogStash][logstash] 1.3.3


Set Up an RPM Build Environment under CentOS
--------------------------------------------

More info: [Set Up an RPM Build Environment][prepare-rpm].

    yum install rpm-build make gcc
    mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
    echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros

Another way:

    yum install rpmdevtools
    rpmdev-setuptree


Prepare
-------

    mkdir ~/temp
    cd ~/temp/
    git clone https://github.com/dreadatour/logstash-specs.git


Build ElasticSearch RPM
-----------------------

    cp -vr ~/temp/logstash-specs/elasticsearch/* ~/rpmbuild/
    cd ~/rpmbuild/
    rpmbuild -v -bb SPECS/elasticsearch.spec

Result RPM:

    ls ~/rpmbuild/RPMS/x86_64/elasticsearch-0.90.9-1.el6.x86_64.rpm


See also
--------
* [github.com/tavisto/elasticsearch-rpms][elasticsearch-rpms]
* [KIBANA + ELASTICSEARCH + LOGSTASH + REDIS ON RHEL 6][logstash-install]


[elasticsearch]: http://www.elasticsearch.com/
[logstash]: https://http://logstash.net/
[prepare-rpm]: http://wiki.centos.org/HowTos/SetupRpmBuildEnvironment
[elasticsearch-rpms]: https://github.com/tavisto/elasticsearch-rpms
[logstash-install]: http://cleversoft.wordpress.com/2013/04/05/887/
