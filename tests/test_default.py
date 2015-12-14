def test_etcd_installed(File):
    for f in ['/usr/local/sbin/etcd', '/usr/local/sbin/etcdctl']:
        file = File(f)

        assert file.exists


def test_cluster_configured(Command):
    address = Command('facter ipaddress_eth1').stdout
    cmd = ('curl -qs '
           'http://{0}:2379/v2/machines | '
           'grep -o 2379 | '
           'wc -l').format(address)

    assert Command.check_output(cmd) == '3'
