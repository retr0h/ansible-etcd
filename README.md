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


Dependencies
------------
There are no dependencies of ansible-etcd.  If you are deploying to CoreOS, however, it is assumed that you have already bootstapped python per [coreos-bootstrap](https://github.com/defunctzombie/ansible-coreos-bootstrap).

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
