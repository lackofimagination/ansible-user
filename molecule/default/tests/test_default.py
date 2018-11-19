import os
from passlib.hash import sha512_crypt

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user(host):
    u = host.user('test')

    assert u.name == 'test'
    assert sha512_crypt.verify('test_password', u.password)
    assert 'test' in u.groups


def test_authorized_key(host):
    f = host.file('/home/test/.ssh/authorized_keys')

    assert f.exists
