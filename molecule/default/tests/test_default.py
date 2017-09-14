import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_command(host):
    if host.system_info.distribution in ['debian', 'ubuntu']:
        service_name = 'bind9'
    elif host.system_info.distribution in ['centos', 'arch']:
        service_name = 'named'
    assert host.service(service_name).is_enabled
    assert host.service(service_name).is_running
