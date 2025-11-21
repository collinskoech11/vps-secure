#!/bin/bash
# Move to project directory
cd /home/ubuntu/vps-secure

# Activate virtual environment
source /home/ubuntu/vps-secure/venv/bin/activate

# Full path to gunicorn executable
/home/ubuntu/vps-secure/venv/bin/gunicorn vpssecureserver.wsgi:application \
  --bind 127.0.0.1:8000 \
  --workers 3 \
  --timeout 90
