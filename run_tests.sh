#!/usr/bin/env bash

# Change to directory where this script is located.
cd "$(dirname "$0")"

cd confcomp

nosetests -v -s
