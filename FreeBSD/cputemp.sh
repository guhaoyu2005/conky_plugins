#!/bin/sh
#
# Conky CPU temp plugin
# FreeBSD specific. Do NOT use on other OSes.
# 
# make sure set coretemp_load="YES" in loader.conf
temp=$(sysctl -n dev.cpu.$1.temperature | sed 's/.$//')
echo ${temp}°C

