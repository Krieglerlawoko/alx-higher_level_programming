#!/bin/bash
# URL taken as argument and sent GET request to URL displayed body of response
curl -s "$1" -H "X-School-User-Id: 98"
