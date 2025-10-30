# 🏏 IPL Victory Prediction - Complete Installation Guide

## 📦 Package Contents

This ZIP file contains the complete IPL Victory Analysis and Prediction project:

```
IPL-Victory-Analysis-with-Prediction/
├── 📁 Dataset/                          [20.5 MB - IPL Data 2008-2022]
│   ├── IPL_Ball_by_Ball_2008_2022.csv
│   └── IPL_Matches_2008_2022.csv
├── 📁 templates/                        [HTML Templates]
│   ├── index.html
│   └── prediction.html
├── 📁 static/                           [CSS Styling]
│   └── style.css
├── 📓 Analysis.ipynb                    [Data Analysis Notebook]
├── 📓 Prediction.ipynb                  [Model Training Notebook]
├── 🧠 IPL_Prediction_Model.pkl          [Pre-trained ML Model]
├── 🐍 app.py                            [Flask Web Application]
├── 📦 requirements.txt                  [Python Dependencies]
├── 📄 README.md                         [Project Documentation]
└── 📜 LICENSE                           [Project License]
```

**Total Size:** ~16 MB (compressed) | ~91 MB (uncompressed)

---

## ⚡ Quick Start (3 Steps)

### Step 1: Extract the ZIP file
```bash
# Windows: Right-click → Extract All
# Mac: Double-click the ZIP file
# Linux: unzip IPL-Victory-Analysis-with-Prediction.zip
```

### Step 2: Install Dependencies
```bash
cd IPL-Victory-Analysis-with-Prediction
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python app.py
```

**Open your browser:** http://localhost:5000

---

## 🖥️ Detailed Installation Instructions

### For Windows Users

1. **Install Python** (if not already installed)
   - Download Python 3.8+ from: https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"
   - Verify: Open CMD and type `python --version`

2. **Extract the Project**
   - Right-click on `IPL-Victory-Analysis-with-Prediction.zip`
   - Select "Extract All"
   - Choose a location (e.g., `C:\Projects\`)

3. **Open Command Prompt**
   - Press `Win + R`
   - Type `cmd` and press Enter
   - Navigate to project folder:
     ```cmd
     cd C:\Projects\IPL-Victory-Analysis-with-Prediction
     ```

4. **Install Dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```cmd
   python app.py
   ```

6. **Access the Website**
   - Open Chrome/Firefox/Edge
   - Go to: http://localhost:5000

---

### For Mac Users

1. **Install Python** (if not already installed)
   - Open Terminal (Cmd + Space, type "Terminal")
   - Install Homebrew (if not installed):
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Install Python:
     ```bash
     brew install python
     ```

2. **Extract the Project**
   - Double-click `IPL-Victory-Analysis-with-Prediction.zip`
   - Or use Terminal:
     ```bash
     unzip IPL-Victory-Analysis-with-Prediction.zip
     ```

3. **Navigate to Project**
   ```bash
   cd IPL-Victory-Analysis-with-Prediction
   ```

4. **Create Virtual Environment** (Recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Application**
   ```bash
   python app.py
   ```

7. **Access the Website**
   - Open Safari/Chrome
   - Go to: http://localhost:5000

---

### For Linux Users

1. **Install Python** (Usually pre-installed)
   ```bash
   # Check version
   python3 --version
   
   # If not installed (Ubuntu/Debian)
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   
   # For Fedora/RHEL
   sudo dnf install python3 python3-pip
   ```

2. **Extract the Project**
   ```bash
   unzip IPL-Victory-Analysis-with-Prediction.zip
   cd IPL-Victory-Analysis-with-Prediction
   ```

3. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the Website**
   - Open browser: http://localhost:5000

---

## 📋 System Requirements

### Minimum Requirements
- **OS:** Windows 7+, macOS 10.12+, or Linux
- **Python:** 3.8 or higher
- **RAM:** 2 GB minimum
- **Disk Space:** 500 MB free space
- **Browser:** Chrome, Firefox, Safari, or Edge (latest version)

### Recommended Requirements
- **OS:** Windows 10+, macOS 11+, or Ubuntu 20.04+
- **Python:** 3.10 or higher
- **RAM:** 4 GB or more
- **Disk Space:** 1 GB free space

---

## 📚 Dependencies Installed

When you run `pip install -r requirements.txt`, these packages are installed:

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | Latest | Web framework for the application |
| pandas | Latest | Data manipulation and CSV handling |
| scikit-learn | Latest | Machine learning algorithms |
| joblib | Latest | Model loading and saving |

Additional dependencies (auto-installed):
- numpy (for numerical operations)
- scipy (for scientific computing)
- Jinja2 (for HTML templating)
- Werkzeug (for WSGI utilities)

---

## 🚀 Running the Application

### Method 1: Standard Run
```bash
python app.py
```
- Server runs on: http://localhost:5000
- Press `Ctrl+C` to stop

### Method 2: Custom Port
```bash
python -c "from app import app; app.run(port=8080)"
```
- Server runs on: http://localhost:8080

### Method 3: Debug Mode (For Development)
```python
# Edit app.py, change last line to:
app.run(debug=True, host='0.0.0.0')
```

### Method 4: Production Server (Advanced)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 📖 How to Use the Application

### 1. Homepage
- Open http://localhost:5000
- Click "Prediction" button

### 2. Make a Prediction
Fill in the match details:
- **Batting Team:** Select the team batting second (chasing)
- **Bowling Team:** Select the opponent team
- **City:** Select the match venue
- **Runs Left:** How many runs needed to win (e.g., 50)
- **Balls Left:** How many balls remaining (e.g., 30)
- **Wickets Left:** Wickets in hand (e.g., 5)
- **Target:** Total target score (e.g., 180)

### 3. View Results
- Click "Predict" button
- See animated win probabilities for both teams
- Results show percentage chance of winning

---

## 🔧 Troubleshooting

### Problem: "Python is not recognized"
**Solution:**
- Windows: Add Python to PATH (reinstall with "Add to PATH" checked)
- Mac/Linux: Use `python3` instead of `python`

### Problem: "No module named 'flask'"
**Solution:**
```bash
pip install flask
# Or install all dependencies:
pip install -r requirements.txt
```

### Problem: "Port 5000 is already in use"
**Solution:**
```bash
# Windows - Kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F

# Mac/Linux
lsof -ti:5000 | xargs kill -9

# Or use different port
python -c "from app import app; app.run(port=8080)"
```

### Problem: "InconsistentVersionWarning" for scikit-learn
**Solution:** This is just a warning, the app works fine. To fix:
```bash
pip install scikit-learn==1.4.0
```

### Problem: "Can't access from other devices"
**Solution:** Edit app.py, change last line to:
```python
app.run(debug=False, host='0.0.0.0')
```
Then access from other devices: http://YOUR_IP:5000

---

## 📊 Working with Jupyter Notebooks

### Install Jupyter
```bash
pip install jupyter notebook
```

### Open Analysis Notebook
```bash
jupyter notebook Analysis.ipynb
```

### Open Prediction/Training Notebook
```bash
jupyter notebook Prediction.ipynb
```

---

## 🎓 Project Features

### ✅ What This Application Does
1. **Data Analysis:** Analyze 15 years of IPL data (2008-2022)
2. **Match Prediction:** Predict win probability during a live match
3. **ML Model:** Uses Random Forest algorithm trained on historical data
4. **Web Interface:** Modern, responsive UI with animations
5. **Real-time Results:** Instant predictions with visual progress bars

### ✅ Technologies Used
- **Backend:** Python + Flask
- **Frontend:** HTML5 + CSS3 + JavaScript
- **ML:** scikit-learn (Random Forest Classifier)
- **Data:** pandas (CSV processing)
- **UI Framework:** Bootstrap 5

---

## 📁 File Descriptions

### Core Application Files
- **app.py** - Flask web server and prediction logic
- **requirements.txt** - Python package dependencies
- **IPL_Prediction_Model.pkl** - Pre-trained ML model (65MB)

### Data Files
- **IPL_Ball_by_Ball_2008_2022.csv** - Ball-by-ball match data
- **IPL_Matches_2008_2022.csv** - Match summaries and results

### Web Interface
- **templates/index.html** - Homepage
- **templates/prediction.html** - Prediction page
- **static/style.css** - Modern UI styling

### Notebooks (Optional)
- **Analysis.ipynb** - Exploratory data analysis
- **Prediction.ipynb** - Model training code

---

## 🌐 Deployment Options

### Deploy to Render.com (Free)
1. Create account at https://render.com
2. Connect GitHub repository
3. Create New Web Service
4. Select Python environment
5. Build command: `pip install -r requirements.txt`
6. Start command: `python app.py`

### Deploy to Heroku (Free Tier)
```bash
# Install Heroku CLI
heroku login
heroku create ipl-prediction-app
git push heroku main
```

### Deploy to PythonAnywhere
1. Upload ZIP file
2. Extract in web console
3. Set up web app with Flask
4. Configure WSGI file

---

## 🔐 Security Notes

- This is a development server (Flask built-in)
- For production, use: Gunicorn, uWSGI, or similar
- Don't expose to public internet without proper security
- Keep dependencies updated

---

## 📞 Support & Contact

**Project Repository:** https://github.com/neerajcodes888/IPL-Victory-Analysis-with-Prediction

**Issues?** Create an issue on GitHub

**Documentation:** See README.md in project folder

---

## 📄 License

This project is licensed under the Eclipse Public License 2.0 (EPL 2.0)

---

## ✨ Quick Reference Commands

```bash
# Extract ZIP
unzip IPL-Victory-Analysis-with-Prediction.zip

# Navigate to project
cd IPL-Victory-Analysis-with-Prediction

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Open in browser
http://localhost:5000

# Stop server
Ctrl + C
```

---

**🎉 You're all set! Enjoy predicting IPL match outcomes!** 🏆
