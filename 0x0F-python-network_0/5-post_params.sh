#!/bin/bash
# Bash script that sends a POST request to the passed URL, and displays the body of the response
curl -s -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
