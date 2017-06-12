#!/usr/bin/env bash

if [ "$1" = "init" ]; then
	echo "Running init, staying alive for new exec instructions..."
	while true;
	do sleep 10;
	done
fi
