from flask import Flask, render_template, request, jsonify
import os
import sys

# Add the parent directory to the path so we can import app.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the main application
from app import app as application

# Vercel requires this specific variable name
app = application

# This is needed for Vercel's serverless environment
if __name__ == "__main__":
    app.run(debug=True, port=5001)
else:
    # This makes it work with Vercel's serverless environment
    pass
