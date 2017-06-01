#!/usr/bin/env bash

if [ "$1" = "train" ]; then
	echo "Running training..."
	python /main.py train
fi

if [ "$1" = "test" ]; then
	echo "Running test..."
	python /main.py test
fi
