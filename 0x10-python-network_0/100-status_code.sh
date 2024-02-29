#!/bin/bash
# request sent to URL and passed as argument. status code of response only displayed
curl -s -L -X HEAD -w "%{http_code}" "$1"
