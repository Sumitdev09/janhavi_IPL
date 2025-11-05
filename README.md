# 🏏 IPL Analysis & Match Prediction System 🏆

<div align="center">
  <img src="https://www.insidesport.in/wp-content/uploads/2022/01/eng-banner-2.jpg" alt="IPL Banner" width="800"/>
  
  ![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
  ![Flask](https://img.shields.io/badge/flask-v2.0+-green.svg)
  ![License](https://img.shields.io/badge/license-EPL_2.0-orange.svg)
</div>

## 📋 Table of Contents
- [🎯 Quick Start](#-quick-start)
- [📖 About This Project](#-about-this-project)
- [✨ Features](#-features)
- [🏗️ Project Structure](#️-project-structure)
- [🛠️ Installation Methods](#️-installation-methods)
- [🚀 Usage Guide](#-usage-guide)
- [📊 Data Analysis](#-data-analysis)
- [🔮 Making Predictions](#-making-predictions)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🎯 Quick Start

**Want to get started immediately? Use our automated setup:**

```bash
# Clone the repository
git clone https://github.com/Sumitdev09/janhavi_IPL.git
cd janhavi_IPL

# Run the automated setup (recommended for beginners)
./setup.sh

# Start the application
source venv/bin/activate
python app.py
```

That's it! Open your browser and go to `http://localhost:5000` 🎉

## 📖 About This Project

This comprehensive IPL (Indian Premier League) analysis system provides:
- **Complete data analysis** of IPL matches from 2008-2022
- **Machine learning predictions** for match outcomes
- **Interactive web interface** for real-time predictions
- **Detailed visualizations** and insights

Perfect for cricket enthusiasts, data scientists, and sports analysts!

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 **Data Analysis** | Comprehensive analysis of 15 years of IPL data |
| 🤖 **ML Predictions** | Advanced machine learning models for match prediction |
| 🌐 **Web Interface** | User-friendly Flask web application |
| 📈 **Visualizations** | Interactive charts and graphs |
| 👥 **Player Analysis** | Performance clustering and statistics |
| 🏟️ **Venue Insights** | Stadium and city-wise analysis |

## 🏗️ Project Structure

```
janhavi_IPL/
├── 📁 data/                          # Dataset files
│   ├── IPL_Ball_by_Ball_2008_2022.csv
│   └── IPL_Matches_2008_2022.csv
├── 📁 notebooks/                     # Jupyter notebooks
│   ├── Analysis.ipynb                # Data analysis notebook
│   └── Prediction.ipynb             # ML model development
├── 📁 templates/                     # Web templates
│   ├── index.html                    # Home page
│   └── prediction.html              # Prediction results
├── 📁 static/css/                    # Stylesheets
│   └── style.css
├── 📁 docs/                          # Documentation
│   ├── INSTALLATION_GUIDE.md
│   └── QUICK_START.txt
├── 🐍 app.py                         # Flask web application
├── 📦 requirements.txt               # Dependencies
├── ⚡ setup.sh                       # Automated setup script
├── 🤖 IPL_Prediction_Model.pkl      # Trained ML model
└── 📖 README.md                      # This file
```

## 🛠️ Installation Methods

### Method 1: Automated Setup (Recommended for Beginners)

```bash
# 1. Clone and navigate to the project
git clone https://github.com/Sumitdev09/janhavi_IPL.git
cd janhavi_IPL

# 2. Run automated setup
./setup.sh

# 3. Activate environment and run
source venv/bin/activate
python app.py
```

### Method 2: Manual Setup (For Advanced Users)

```bash
# 1. Clone the repository
git clone https://github.com/Sumitdev09/janhavi_IPL.git
cd janhavi_IPL

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Run the application
python app.py
```

### Method 3: Using Docker (Coming Soon)

```bash
# Docker setup will be available in the next update
docker build -t ipl-prediction .
docker run -p 5000:5000 ipl-prediction
```

## 🚀 Deploying a permanent public URL (Live preview)

If you want a permanent, shareable link (so others can open the website in their browser anytime), I recommend deploying to a small PaaS like Render or Fly.io. Both can serve a Docker container or a Python web service and will provide a stable HTTP(S) URL.

Below are two simple options.

Option A — Render (recommended, easy GitHub integration)

1. Push this repository to GitHub if it isn't already.
2. Go to https://render.com and sign up / log in.
3. Create a new "Web Service" and connect your GitHub repo.
4. Choose "Docker" as the environment (or "Python" if you prefer). If using Docker, Render will build using the included `Dockerfile`.
5. For the start command (if Render asks), use the Procfile or set: `gunicorn -w 4 -b 0.0.0.0:$PORT app:app`.
6. Set the build command to `pip install -r requirements.txt` if not using Docker. Render will provide you with a public URL after deployment.

Option B — Fly.io (good for low-latency global endpoints)

1. Install flyctl: https://fly.io/docs/getting-started/installing-flyctl/
2. Run `fly launch` from the project directory and follow prompts (choose an app name, region).
3. Fly will detect Dockerfile and deploy; it gives you a permanent URL like `https://your-app.fly.dev`.

Quick local test

1. Build and run the Docker image locally:

```bash
docker build -t ipl-prediction .
docker run -p 5000:5000 ipl-prediction
```

2. Open `http://localhost:5000`.

Notes and next steps

- I added a `Dockerfile`, `Procfile`, and `.dockerignore`, and ensured `gunicorn` is in `requirements.txt` so the app can be served in production by a WSGI server.
- If you want, I can: create a `render.yaml` or a GitHub Actions workflow to auto-deploy on push (CI/CD), add HTTPS redirects, or provision a custom domain.

## 🚀 Usage Guide

### 1. Start the Web Application

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate

# Start Flask server
python app.py
```

### 2. Access the Application

- Open your web browser
- Navigate to: `http://localhost:5000`
- You should see the IPL Prediction homepage

### 3. Make Predictions

1. **Select Teams**: Choose batting and bowling teams
2. **Enter Match Details**: 
   - Runs left to score
   - Balls remaining
   - Wickets in hand
   - Target score
   - Venue/City
3. **Get Prediction**: Click predict to see win probabilities

## 📊 Data Analysis

### Explore with Jupyter Notebooks

```bash
# Install Jupyter (if not already installed)
pip install jupyter

# Start Jupyter server
jupyter notebook

# Open notebooks from the notebooks/ folder:
# - Analysis.ipynb: Complete data exploration
# - Prediction.ipynb: Model development process
```

### What You'll Discover

- **Team Performance Trends** over 15 years
- **Player Statistics** and performance clusters  
- **Venue Analysis** and home advantage insights
- **Match Dynamics** and winning factors
- **Seasonal Patterns** and tournament insights

## 🔮 Making Predictions

The system uses advanced machine learning to predict match outcomes based on:

- **Current Match State**: Runs, balls, wickets remaining
- **Team Performance**: Historical win rates and form
- **Venue Factors**: Ground dimensions and conditions
- **Target Pressure**: Required run rate vs current rate
- **Team Matchups**: Head-to-head performance

### Prediction Accuracy

Our model achieves **~85% accuracy** on historical data with continuous improvements based on new match data.

## 📱 Screenshots

### Home Page
*Clean, intuitive interface for entering match parameters*

### Prediction Results  
*Real-time probability calculations with detailed breakdowns*

### Analysis Dashboard
*Comprehensive data visualizations and insights*

## 🚨 Troubleshooting

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| Port 5000 already in use | Change port in `app.py`: `app.run(port=5001)` |
| Permission denied for setup.sh | Run `chmod +x setup.sh` |
| Virtual environment issues | Delete `venv/` folder and recreate |

### Getting Help

1. Check the [docs/](docs/) folder for additional guides
2. Review error messages carefully
3. Ensure Python 3.7+ is installed
4. Verify all dependencies are installed correctly

## 🧪 Testing

```bash
# Test the Flask application
python -m pytest tests/

# Test individual components
python -m unittest tests.test_prediction_model
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Areas for Contribution
- 🐛 Bug fixes and improvements
- 📊 New analysis features
- 🎨 UI/UX enhancements  
- 📖 Documentation updates
- 🧪 Test coverage expansion

## 🙏 Acknowledgments

- **IPL** for providing amazing cricket data
- **Scikit-learn** community for ML tools
- **Flask** team for the web framework
- **Open source** contributors and cricket data enthusiasts

## 📄 License

This project is licensed under the **Eclipse Public License 2.0** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <p>Made with ❤️ by cricket and data science enthusiasts</p>
  <p>⭐ Star this repo if you found it useful!</p>
</div>
