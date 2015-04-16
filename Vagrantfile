# encoding: UTF-8

Vagrant.configure('2') do |config|
  config.vm.box = 'hashicorp/precise64'
  # https://github.com/mitchellh/vagrant/issues/5205
  config.ssh.insert_key = false
  config.vm.provision 'ansible' do |ansible|
    ansible.playbook = 'vagrant/site.yml'
    ansible.limit = 'all'
    ansible.sudo = true
    ansible.host_key_checking = false
    ansible.groups = {
      'etcd' => ['etcd-1', 'etcd-2', 'etcd-3']
    }
    ansible.extra_vars = {
      etcd_interface: 'eth1'
    }
  end

  (1..3).each do |i|
    vm_name = "etcd-#{i}"
    config.vm.define vm_name do |c|
      c.vm.host_name = vm_name
      c.vm.network 'private_network', ip: "192.168.30.#{11 + i}" # eth1
    end
  end
end
