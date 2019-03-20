#!/usr/bin/env python
from __future__ import unicode_literals, print_function
import yaml
from os import path
from netmiko import ConnectHandler
from getpass import getpass

home_dir = path.expanduser("~")
filename = path.join(home_dir, ".servers.yml")

with open(filename) as f:
    servers = yaml.load(f)

password = getpass()
net_connect = ConnectHandler(**servers["localhost"])
checkupdate = net_connect.send_command("apt-get update; apt-get -s upgrade")

print(checkupdate)
