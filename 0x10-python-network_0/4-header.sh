#!/bin/bash
#takes a URL, sends a GET request with a custom header, and displays the body
curl -sH "X-School-User-Id: 98" "$1"
