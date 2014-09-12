# Logstash SPECS for CentOS

All that you need to build CentOS RPMs for:

* [ElasticSearch][elasticsearch] 1.3.2
* [Logstash][logstash] 1.4.2
* [Kibana][kibana] 3.1.0


## Hot to build

Clone repository and prepare RPM build environment.

    $ git clone https://github.com/pzinovkin/logstash-specs.git
    $ cd logstash-specs
    $ make init

Now you can `make` something:

    $ make
    Please choose one of the following target:
      init
      clean
      elasticsearch
      kibana
      logstash
    $ make elasticsearch

## Building with VritualBox 

Install VirtualBox and Vagrant. Initialize virtual machine.

    $ vagrant up

SSH to newly created machine. Directory will be changed automatically.

    $ vagrant ssh
    $ make logstash

See also
--------
* [github.com/tavisto/elasticsearch-rpms][elasticsearch-rpms]


[elasticsearch]: http://www.elasticsearch.com/
[logstash]: https://http://logstash.net/
[kibana]: http://www.elasticsearch.org/overview/kibana/
[prepare-rpm]: http://wiki.centos.org/HowTos/SetupRpmBuildEnvironment
[elasticsearch-rpms]: https://github.com/tavisto/elasticsearch-rpms
