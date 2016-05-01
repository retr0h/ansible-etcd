etcd
====

A role which installs and manages a clustered etcd.

Role ready status
-----------------

[![Galaxy](http://img.shields.io/badge/galaxy-ansible--etcd-blue.svg?style=flat-square)](https://galaxy.ansible.com/list#/roles/1206)

Requirements
------------

Ansible 1.9 or 2.0

Role Variables
--------------

See defaults/main.yml

Dependencies
------------

None

Example Playbook
----------------

    - hosts: etcd
      roles:
        - retr0h.etcd

Testing
-------

Tests are performed by [Molecule](http://molecule.readthedocs.org/en/latest/).

    $ make
    $ source venv/bin/activate
    $ molecule test

License
-------

MIT
