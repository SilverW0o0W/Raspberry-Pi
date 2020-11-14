#!/bin/bash
SC_KEY=$1

sc_key = "$SC_KEY" >> /etc/notice_ip/notice_ip.toml
cp src/notice_ip.service /lib/systemd/system/notice_ip.service
cp -r src/python /usr/local/src/notice_ip
pip install --no-cache-dir -r requirements.txt
systemctl daemon-reload
systemctl enable notice_ip.service
