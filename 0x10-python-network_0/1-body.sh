#!/bin/bash
# display  the body
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
result=$(curl -s -w "$1")
if [ "$result" -eq 200 ]; then
	curl -s "$1"
else
    echo "Received non-200 response: HTTP status $result"
fi
