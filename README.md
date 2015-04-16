etcd
====

A role which installs and manages a clustered etcd (v2.0.9).

Role ready status
-----------------

[![Build Status](http://img.shields.io/travis/retr0h/ansible-etcd.svg?style=flat-square)](https://travis-ci.org/retr0h/ansible-etcd)
[![Galaxy](http://img.shields.io/badge/galaxy-ansible--etcd-blue.svg?style=flat-square)](https://galaxy.ansible.com/list#/roles/1206)

Requirements
------------

None

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

    $ vagrant up --no-provision
    $ vagrant provision

License
-------

MIT
