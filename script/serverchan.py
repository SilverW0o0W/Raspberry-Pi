#!/usr/bin/env python3.6
# -*- encoding: utf-8 -*-

import requests
import urllib3

urllib3.disable_warnings()


def send(title, content, sc_key):
    url = "https://sc.ftqq.com/{}.send".format(sc_key)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "text": title,
        "desp": content,
    }
    try:
        requests.post(url, data=data, headers=headers, verify=False)
    except Exception as e:
        pass
