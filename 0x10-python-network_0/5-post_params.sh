#!/bin/bash
# URL taken and POST request made to URL then body of response displayed
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
