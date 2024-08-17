#!/bin/bash

# Check if requirements.txt exists in the current directory
if [ ! -f "requirements.txt" ]; then
  echo "Error: requirements.txt not found in the current directory."
  exit 1
fi

# Install the required packages using pip
echo "Installing packages from requirements.txt..."
pip install -r requirements.txt --no-cache

# Check if the installation was successful
if [ $? -ne 0 ]; then
  echo "Error: Failed to install some packages. Please check the output above."
  exit 1
else
  echo "All packages installed successfully."
fi