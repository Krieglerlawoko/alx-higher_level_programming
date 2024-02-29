#!/bin/bash
# DELETE request sent to URL and passed as first argument then body of response displayed
curl -s "$1" -X DELETE
