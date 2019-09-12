#!/usr/bin/env python3.6
# -*- encoding: utf-8 -*-

import os
import sys
import socket

import toml

import serverchan


def get_host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def load_config(file_path):
    with open(file_path, "r") as f:
        return toml.load(f)


def run(sc_key):
    ip = get_host_ip()
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
