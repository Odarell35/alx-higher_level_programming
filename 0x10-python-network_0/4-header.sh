#!/bin/bash
#sends a GET request for the response.
curl -s "$1" -X GET -H 'X-School-User-Id: 98'
