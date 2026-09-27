#!/bin/bash

python3 /app/generate.py

# Keep container running (or serve files)
python3 -m http.server 8000