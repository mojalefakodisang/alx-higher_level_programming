#!/usr/bin/env bash
curl -I -s "$1" | grep -i "Content-Length" | awk '{print $2}'
