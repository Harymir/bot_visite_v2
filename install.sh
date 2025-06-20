#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is required but not installed."
    exit 1
fi

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

echo "Installation complete! Run the bot with: python bot_visite.py"
