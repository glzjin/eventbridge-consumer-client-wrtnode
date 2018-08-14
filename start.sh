#!/bin/sh
cd `dirname $0`
sh stop.sh
nohup python3 main.py >> /dev/null 2>&1 &
