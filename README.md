etcd
====

A role which installs and manages etcd.

Role ready status
-----------------

[![Build Status](http://img.shields.io/travis/retr0h/ansible-etcd.svg?style=flat-square)](https://travis-ci.org/retr0h/ansible-etcd)
[![Galaxy](http://img.shields.io/badge/galaxy-ansible--etcd-blue.svg?style=flat-square)](https://galaxy.ansible.com/list#/roles/1206)

Requirements
------------

None

Role Variables
--------------

* `etcd_version` - Version of etcd to install. (default: v0.4.5)
* `etcd_platform` - Platform of etcd to install. (default: linux)
* `etcd_arch` - Architecture of etcd to install. (default: amd64)
* `etcd_release` - Name of etcd file used by unarchive and download.
                   Composed of `etcd_version`, `etcd_platform`, and
                   `etcd_arch`.
* `etcd_download_url` - URL pointing to the etcd archive.  Composed of
                        `etcd_version` and `etcd_release`.
* `etcd_download_dir` - Directory to download and unarchive into. 
                        (default: /usr/local/src)
* `etcd_dir` - Directory hosting the etcd binaries. (default: /usr/local/sbin)
* `etcd_data_dir` - Path to etcd's data directory.
                    (default: /var/cache/etcd/state)
* `etcd_cmd` - Path to the etcd command. (default: `etcd_dir`/etcd)
* `etcd_interface` - Interface's IPv4 address to bind to. (default: lo)
* `etcd_client_port` - The client port. (default: 4001)
* `etcd_peer_port` - The server-to-server port. (default: 7001)
* `etcd_addr` -  The public IPv4:port used for client communication.
                 (default: `etcd_interface`:`etcd_client_port`) 
* `etcd_peer_addr` - The public IPv4:port used for peer communication.
                 (default: `etcd_interface`:`etcd_peer_port`) 
* `etcd_cluster` - Flag to cluster or not. (default: None)
* `etcd_peers_group` - The Ansible peers in cluster.
                      (default: etcd-peers)

Dependencies
------------

None

Example Playbook
----------------

    - hosts: etcd-seed-node
      roles:
        - retr0h.etcd

    - hosts: etcd-remaining-nodes
      roles:
        - { role: retr0h.etcd, etcd_cluster: True }

License
-------

MIT
