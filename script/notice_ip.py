#!/usr/bin/env python3.6
# -*- encoding: utf-8 -*-

import os
import sys
import socket
import time

import toml

import serverchan


def get_host_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        except OSError:
            ip = None
        return ip


def load_config(file_path):
    with open(file_path, "r") as f:
        return toml.load(f)


def run(sc_key):
    now = int(time.time())
    ip = None
    while not ip:
        ip = get_host_ip()
        time.sleep(1)
    title = "树莓派IP:{}".format(ip.replace(".", "_"))
    content = "{}\n{}".format(ip, now)
    serverchan.send(title, content, sc_key)


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
