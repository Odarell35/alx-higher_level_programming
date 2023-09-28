#!/bin/bash
# display  the body
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
curl -sfL "$1"
