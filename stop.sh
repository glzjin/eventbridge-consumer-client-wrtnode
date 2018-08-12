#!/bin/sh
cd `dirname $0`
eval $(ps  | grep "[ *]python main\\.py" | awk '{print "kill "$1}')
