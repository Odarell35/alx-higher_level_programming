#!/bin/bash
# Get The body  size  from outgoing
curl -sI "$1" | grep 'Content-Length:' | cut -c 17-
