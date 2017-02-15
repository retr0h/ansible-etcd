import re

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('f', ['/usr/local/sbin/etcd',
                               '/usr/local/sbin/etcdctl'])
def test_etcd_installed(File, f):
    file = File(f)

    assert file.exists


def test_cluster_configured(Interface, Command):
    address = Interface('eth0').addresses[0]
    endpoint = 'http://{}:2379'.format(address)
    cmd = 'etcdctl --endpoints {} cluster-health'.format(endpoint)
    out = Command.check_output(cmd)

    assert 6 == len(re.findall(r'member [\d\w]+ is healthy', out))
    assert 'cluster is healthy' in out
