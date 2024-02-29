#!/bin/bashi
# URL taken and all HTTP methods accepted by server displayed
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
