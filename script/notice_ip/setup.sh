#!/bin/bash
cp notice_ip.service /lib/systemd/system/notice_ip.service
systemctl daemon-reload
systemctl enable notice_ip.service
sudo pip install requirements.txt
