#!/bin/bash
# Displays methods of URL
curl -sIX OPTIONS "$1" | grep -i "Allow" | awk -F ": " '{print $2}'
