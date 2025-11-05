#!/bin/bash
set -o pipefail

log_file="nohup.out"

if [[ -n "$1" ]]; then
    log_file="$1"
fi

clear

while :; do
    cat "$log_file" | grep Epoch | tail -1
    tail -1 "$log_file"
    sleep 2
    clear
done
