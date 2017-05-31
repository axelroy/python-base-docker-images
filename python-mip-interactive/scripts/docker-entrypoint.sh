#!/usr/bin/env bash

if [ "$1" = "train" ]; then
	echo "Running training..."
	python /main.py
fi

if [ "$1" = "test" ]; then
	echo "Running test..."
	python /main.py
fi
