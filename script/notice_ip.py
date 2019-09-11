#!/usr/bin/env python3.6
# -*- encoding: utf-8 -*-

import os
import sys
import socket

import toml

from script import serverchan


def get_local_ip():
    hostname = socket.getfqdn(socket.gethostname())
    return socket.gethostbyname(hostname)


def load_config(file_path):
    with open(file_path, "r") as f:
        return toml.load(f)


def run(sc_key):
    ip = get_local_ip()
    title = "树莓派IP:{}".format(ip.replace(".", "_"))
    serverchan.send(title, ip, sc_key)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("command: command config_file")
        exit(-1)

    config_file_path = sys.argv[1]
    if not os.path.isfile(config_file_path):
        print("command: not find config_file")
        exit(-1)
    config = load_config(config_file_path)
    run(config["sc_key"])
