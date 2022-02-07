What to run
===========

1. Run `ansible-playbook install.yaml` to check assignment 1.
2. Run `deploy-1.yaml` to check challenge 1.
3. Run `deploy-2.yaml` to check challenge 2.

Files created per requirements
------------------------------
- Inventory
- ansible.cfg
- Roles: common, deploy-1, deploy-2

Some commands
-------------
1. installed ansible $ `sudo sh install_ansible.sh`
2. installed $ sudo sh setup-ubuntu.sh  # had to remove `set -e`
3. $ ssh-copy-id -p <port>  root@localhost
4. created ansible.cfg file with overwrite defaults
5. created inventory file
6. $ `ansible-galaxy init common`


# how to filter facts
`ansible all -m setup -a "filter=ansible_hostname" | grep ansible_hostname`
