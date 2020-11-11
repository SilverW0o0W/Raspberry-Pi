#!/bin/bash
sudo su
cp notice_ip.service /lib/systemd/system/notice_ip.service
systemctl daemon-reload
systemctl enable notice_ip.service
pip install --no-cache-dir -r requirements.txt
