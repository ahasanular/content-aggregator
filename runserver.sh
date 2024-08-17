#!/bin/bash

# Check if Django is installed and manage.py is in the current directory
if ! command -v python &>/dev/null || [ ! -f "manage.py" ]; then
  echo "Error: Django is not installed or manage.py not found in the current directory."
  exit 1
fi

# Start the Django development server
echo "Starting Django development server..."
python manage.py runserver

# Check if the server started successfully
if [ $? -ne 0 ]; then
  echo "Error: Failed to start the server. Please check the output above."
  exit 1
fi