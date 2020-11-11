#!/bin/bash
cp notice_ip.service /etc/systemd/system/notice_ip.service
systemctl daemon-reload
systemctl enable notice_ip.service
pip install requirements.txt
