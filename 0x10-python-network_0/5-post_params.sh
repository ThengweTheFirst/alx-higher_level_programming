#!/bin/bash
# takes in a URL as an argument, and
curl -sX -F POST 'email=test@gmail.com' -F 'subject=I will always be there for PLD' "$1"
