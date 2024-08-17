#!/bin/bash

# Check if Django is installed and manage.py is in the current directory
if ! command -v python &>/dev/null || [ ! -f "manage.py" ]; then
  echo "Error: Django is not installed or manage.py not found in the current directory."
  exit 1
fi

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Check if migrations were successful
if [ $? -ne 0 ]; then
  echo "Error: Migrations failed. Please check the output above."
  exit 1
fi