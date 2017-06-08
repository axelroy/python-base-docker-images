#!/usr/bin/env bash

if [ "$1" = "init" ]; then
	echo "Running init, staying alive for new exec instructions..."
	while true;
	do sleep 10;
	done
fi

if [ "$1" = "train" ]; then
	echo "Running training..."
	python /main.py train
fi

if [ "$1" = "test" ]; then
	echo "Running test..."
	python /main.py test
fi
