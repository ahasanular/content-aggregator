#!/bin/bash

# Check if the install-dependencies.sh script exists and is executable
if [ -f "./install-dependencies.sh" ] && [ -x "./install-dependencies.sh" ]; then
  echo "Running migrations..."
  ./install-dependencies.sh
else
  echo "Error: install-dependencies.sh not found or not executable."
  exit 1
fi

# Check if the migrate.sh script exists and is executable
if [ -f "./migrate.sh" ] && [ -x "./migrate.sh" ]; then
  echo "Running migrations..."
  ./migrate.sh
else
  echo "Error: migrate.sh not found or not executable."
  exit 1
fi

# Check if the create-super-user.sh script exists and is executable
if [ -f "./create-super-user.sh" ] && [ -x "./create-super-user.sh" ]; then
  echo "Running create-super-user..."
  ./create-super-user.sh
else
  echo "Error: create-super-user.sh not found or not executable."
  exit 1
fi

# Check if the runserver.sh script exists and is executable
if [ -f "./runserver.sh" ] && [ -x "./runserver.sh" ]; then
  echo "Running runserver..."
  ./runserver.sh
else
  echo "Error: runserver.sh not found or not executable."
  exit 1
fi