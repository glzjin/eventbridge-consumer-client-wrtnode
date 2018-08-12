#!/bin/sh
cd `dirname $0`
PID=$(ps  | grep "[ *]python main\\.py" | awk '{print $1}')
if [ -z $PID ]; then
  sh start.sh
fi
