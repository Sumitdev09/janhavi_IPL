# 💻 Installation Guide - IPL Analysis Project

## 📋 Prerequisites

Before starting, make sure you have:

- **Python 3.7 or higher** ([Download here](https://python.org))
- **Git** ([Download here](https://git-scm.com))
- **Internet connection** (for package downloads)

### Check Your Python Version
```bash
python --version
# or 
python3 --version
```

## 🎯 Installation Options

### Option 1: Automated Installation (Recommended)

**Perfect for beginners or quick setup:**

```bash
# 1. Get the project
git clone https://github.com/Sumitdev09/janhavi_IPL.git
cd janhavi_IPL

# 2. Run auto-installer
chmod +x setup.sh
./setup.sh

# 3. Start the app
source venv/bin/activate
python app.py
```

### Option 2: Step-by-Step Manual Installation

**For users who want full control:**

#### Step 1: Clone Repository
```bash
git clone https://github.com/Sumitdev09/janhavi_IPL.git
cd janhavi_IPL
```

#### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows
```

#### Step 3: Install Dependencies
```bash
# Upgrade pip
pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt
```

#### Step 4: Verify Installation
```bash
# Check if all packages installed correctly
pip list
```

#### Step 5: Run the Application
```bash
python app.py
```

### Option 3: Development Setup

**For contributors and developers:**

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/janhavi_IPL.git
cd janhavi_IPL

# Create development environment
python3 -m venv venv
source venv/bin/activate

# Install in development mode
pip install -r requirements.txt
pip install jupyter  # For notebook development
pip install pytest   # For testing

# Run tests
pytest tests/
```

## 🚨 Troubleshooting Common Issues

### Issue 1: Python Not Found
**Error**: `python: command not found`

**Solution**:
```bash
# Try python3 instead of python
python3 --version
python3 app.py
```

### Issue 2: Permission Denied (setup.sh)
**Error**: `Permission denied: ./setup.sh`

**Solution**:
```bash
chmod +x setup.sh
./setup.sh
```

### Issue 3: Module Not Found
**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**:
```bash
# Activate virtual environment first
source venv/bin/activate
pip install -r requirements.txt
```

### Issue 4: Port Already in Use
**Error**: `Address already in use: Port 5000`

**Solution**:
```bash
# Kill process using port 5000
sudo lsof -t -i tcp:5000 | xargs kill -9

# OR run on different port by editing app.py:
# Change: app.run(debug=False,host='0.0.0.0')
# To: app.run(debug=False,host='0.0.0.0',port=5001)
```

### Issue 5: Virtual Environment Issues
**Error**: Various venv-related errors

**Solution**:
```bash
# Delete and recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🔧 Advanced Configuration

### Custom Port Configuration
Edit `app.py` to change the default port:
```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)  # Custom port
```

### Environment Variables
Create a `.env` file for custom settings:
```bash
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000
```

### Production Deployment
For production servers:
```bash
# Use gunicorn for production
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📊 Post-Installation Setup

### 1. Verify Web Application
```bash
# Start the app
python app.py

# Test in browser: http://localhost:5000
# You should see the IPL prediction homepage
```

### 2. Test Jupyter Notebooks
```bash
# Install jupyter (if not already done)
pip install jupyter

# Start jupyter
jupyter notebook

# Open notebooks/Analysis.ipynb to test
```

### 3. Verify Data Files
```bash
# Check if data files exist
ls data/
# Should show: IPL_Ball_by_Ball_2008_2022.csv  IPL_Matches_2008_2022.csv

# Check model file
ls *.pkl
# Should show: IPL_Prediction_Model.pkl
```

## 🎉 Success Checklist

- [ ] Python 3.7+ installed and working
- [ ] Virtual environment created and activated
- [ ] All dependencies installed without errors
- [ ] Flask app runs without errors
- [ ] Web interface accessible at http://localhost:5000
- [ ] Prediction form works and returns results
- [ ] Jupyter notebooks open and run (optional)

## 🆘 Still Having Issues?

1. **Check Python Version**: Ensure Python 3.7+
2. **Check Internet**: Required for package downloads
3. **Try Clean Install**: Delete project folder and start over
4. **Check System**: Ensure enough disk space and permissions
5. **Ask for Help**: Create an issue on GitHub with:
   - Your operating system
   - Python version
   - Full error message
   - Steps you tried

## 🚀 What's Next?

After successful installation:
1. Read the main [README.md](../README.md) for detailed usage
2. Try making your first prediction
3. Explore the Jupyter notebooks
4. Contribute improvements!

Happy cricket data analysis! 🏏📊