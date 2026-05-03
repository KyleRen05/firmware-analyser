#!/bin/bash

echo "Please Enter Binary file (.bin)"
read -e file

python3 src/python/main.py $file