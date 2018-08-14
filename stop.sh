#!/bin/sh
cd `dirname $0`
eval $(ps  | grep "[ *]python3 main\\.py" | awk '{print "kill "$1}')
