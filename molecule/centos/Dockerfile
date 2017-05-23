FROM retr0h/centos7-systemd-ansible

RUN /bin/sh -c 'if [ -x "$(command -v yum)" ]; then touch /var/lib/rpm/* && yum makecache fast && yum update -y && yum install -y python sudo yum-plugin-ovl bash && sed -i 's/plugins=0/plugins=1/g' /etc/yum.conf; fi'
