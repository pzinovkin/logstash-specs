# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "chef/centos-6.5"
  config.vm.provision "shell", inline: "
    cd /vagrant;
    rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-6
    yum install -y vim
    make init
    echo 'cd /vagrant' >> /home/vagrant/.bashrc
  "
end
