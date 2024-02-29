#!/bin/bash
# URL taken and sent a request to and size of body diplayed as response
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
