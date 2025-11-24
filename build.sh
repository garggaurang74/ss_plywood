#!/bin/bash
set -e

# Use Python 3.11 if available
python3.11 -m pip install --upgrade pip
python3.11 -m pip install -r requirements.txt
