#!/bin/bash
# Bsh script that takes URL, sends GET request and dispays response body
curl -s "$1" -H "X-School-User-Id: 98"
