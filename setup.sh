#!/bin/bash

# IPL Analysis and Prediction Setup Script
# This script will set up your environment for running the IPL analysis and prediction project

echo "🏏 Setting up IPL Analysis and Prediction Project..."
echo "=================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✅ Python3 found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3."
    exit 1
fi

echo "✅ pip3 found"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📥 Installing required packages..."
pip install -r requirements.txt

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "📋 To run the project:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the Flask app: python app.py"
echo "3. Open your browser and go to: http://localhost:5000"
echo ""
echo "📊 To run Jupyter notebooks:"
echo "1. Install jupyter: pip install jupyter"
echo "2. Start jupyter: jupyter notebook"
echo "3. Open notebooks from the 'notebooks/' folder"
echo ""
echo "Happy analyzing! 🏏📈"