#!/bin/bash
# a request to an URL with curl to displays the size of the body of the response
curl -s "$1" | wc -c
