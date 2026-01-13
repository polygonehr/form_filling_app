import os
import sys
from flask import Flask, render_template, request, jsonify

# Add both web/ and root directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'web'))
sys.path.insert(0, os.path.dirname(__file__))

# Now import your Flask app
try:
    # Adjust this based on your actual file structure
    from app import app as application  # If your main file is web/app.py
except ImportError:
    # Try alternative import paths
    from web.app import app as application

# Vercel requires this specific variable name
app = application

# This is needed for Vercel's serverless environment
if __name__ == "__main__":
    app.run(debug=True, port=5001)
else:
    # This makes it work with Vercel's serverless environment
    pass
