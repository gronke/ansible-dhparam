import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_crontab_exists(host):
    out = host.check_output('/usr/bin/crontab -l')
    desired = "@weekly /usr/bin/openssl dhparam -dsaparam -out "
    "'/etc/ssl/private/dhparam.pem' 4096"
    assert desired in out
