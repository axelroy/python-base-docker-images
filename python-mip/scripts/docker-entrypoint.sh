#!/usr/bin/env bash

if [ "$1" = "compute" ]; then
	echo "Running python-histogram computation..."
	python /main.py
fi
