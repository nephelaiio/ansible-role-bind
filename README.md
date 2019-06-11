# nephelaiio.bind

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-bind.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-bind)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-systemd--service-blue.svg)](https://galaxy.ansible.com/nephelaiio/bind/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/bind) to install and configure bind

## Variables

The following variables allow you to override the state of the bind service
Use ```bind_service_status``` to override the default runtime state of the service
Use ```bind_service_enabled``` to override the default startup state of the service

The following variables allow you to override the default configuration options
Use ```bind_interfaces_ipv4``` and ```bind_interfaces_ipv6``` to override the default interfaces (Global default: [localhost, ansible_default_ipv4.address])bind will listen on
Use ```bind_forwarders``` to override forwarders for the default configuration (Global default: [8.8.8.8, 8.8.4.4])
Use ```bind_packages``` to override the package name for bind (Ubuntu default: bind9)
Use ```bind_conf_options``` to override settings in ```bind_conf_options_path``` (Debian default: /etc/bind/named.conf.options) file
Use ```bind_conf_local``` to override settings in ```bind_conf_local_path``` (Debian default: /etc/bind/named.conf.local) file
Use ```bind_conf_template``` to provide raw configuration for bind; this is mutually exclusive with all other configuration options

## Example Playbook

```
- hosts: servers
  roles:
     - role: bind
       bind_packages_state: latest
```

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](/requirements.txt)

Role is tested against the following distributions (docker images):

  * Ubuntu Bionic
  * Ubuntu Xenial
  * CentOS 7
  * Debian Stretch
  * Arch Linux

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
