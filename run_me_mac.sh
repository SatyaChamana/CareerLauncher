#!/bin/bash
# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed or not added to PATH."
    exit
fi

# Run the Python script
python3 CareersLauncher.py
