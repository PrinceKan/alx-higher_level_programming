#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing,in the body of the response
curl -s -X PUT -H "Content-Type: text/plain" --data "You got me!" 0.0.0.0:5000/catch_me >/dev/null &
