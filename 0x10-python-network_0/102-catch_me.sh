#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing,in the body of the response
curl -s 0.0.0.0:5000/catch_me | sed -n 's/.*\(You got me!\).*/\1/p'1
