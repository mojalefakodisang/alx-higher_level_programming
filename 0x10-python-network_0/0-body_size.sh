#!/bin/bash
# Gets the URL content length
curl -I -s "$1" | grep -i "Content-Length" | awk '{print $2}'
