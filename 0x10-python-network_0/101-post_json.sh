#!/bin/bash
# JSON POST request sent to URL & passed as first argument then body of response displayed
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
