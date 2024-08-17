#!/bin/bash

# Set default values for the superuser
USERNAME="admin"
PASSWORD="000000"

# Check if Django is installed and manage.py is in the current directory
if ! command -v python &>/dev/null || [ ! -f "manage.py" ]; then
  echo "Error: Django is not installed or manage.py not found in the current directory."
  exit 1
fi

# Create the superuser with the specified details
echo "Creating superuser with username: $USERNAME, password: $PASSWORDs"

# Use the environment variable method to pass details to the create superuser command
python manage.py shell <<EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='$USERNAME').exists():
    User.objects.create_superuser('$USERNAME', password='$PASSWORD')
    print("Superuser created successfully.")
else:
    print("Superuser with this username already exists.")
EOF