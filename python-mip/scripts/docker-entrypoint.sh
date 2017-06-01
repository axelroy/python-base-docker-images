#!/usr/bin/env bash

if [ "$1" = "train" ]; then
	echo "Running python-histogram computation..."
	python /main.py train
fi

if [ "$1" = "test" ]; then
	echo "Running python-histogram computation..."
	python /main.py test
fi
