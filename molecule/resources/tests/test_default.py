import os
import re

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('f',
                         ['/usr/local/sbin/etcd', '/usr/local/sbin/etcdctl'])
def test_etcd_installed(host, f):
    file = host.file(f)

    assert file.exists


def test_cluster_configured(host):
    address = host.interface('eth0').addresses[0]
    endpoint = 'http://{}:2379'.format(address)
    cmd = 'etcdctl --endpoints {} cluster-health'.format(endpoint)
    out = host.command.check_output(cmd)

    assert 3 == len(re.findall(r'member [\d\w]+ is healthy', out))
    assert 'cluster is healthy' in out
