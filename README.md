# nephelaiio.bind

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-bind.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-bind)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-systemd--service-blue.svg)](https://galaxy.ansible.com/nephelaiio/bind/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/bind) to install and configure bind

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
  * Ubuntu Xenial
  * CentOS 7
  * Debian Stretch
  * Arch Linux

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
