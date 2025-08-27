# Phishing Website Detection System

## 🚀 Overview

This project is a **Hybrid Phishing Website Detection Tool** built with **Python** and a **Flask web interface**. It combines:

* 🧠 **Rule-based techniques** (simple heuristics)
* 🤖 **Machine Learning models** (Random Forest Classifier)
* 🎨 **Flask UI** for real-time input and result viewing
* 🗂️ Logging to file
* 📄 Optional export to PDF or scan history view

---

## 🔍 Features

* 🧪 Detect phishing URLs using both rules and machine learning
* 📄 Rule-based reasons for detection (e.g. "contains '@'")
* 📦 Feature extraction from URLs
* ✅ Scan history log
* 🎛️ Visual result page with color-coded outcomes
* 🎨 Styled with basic HTML & CSS (Bootstrap optional)
* 🌗 Dark mode toggle (optional enhancement)
* 📥 Export result to PDF (optional)
* 🔊 Voice input support (disabled by default)

---

## 📁 Project Structure

```bash
phishing_detector_project/
├── app.py                      # Flask main app
├── templates/
│   ├── base.html              # Base layout
│   ├── form.html              # URL input form
│   └── result.html            # Result display
│   └── history.html           # Scan history view
├── static/                    # Optional: CSS/JS
├── src/
│   ├── rule_based.py          # Heuristic-based rules
│   ├── ml_based.py            # ML training on basic features
│   ├── ml_custom_features.py  # ML training with custom features
│   ├── hybrid_detector.py     # Combines rule + ML prediction
│   ├── feature_extraction.py  # Extract features from URL
│   └── utils.py               # Logger, timestamp, etc.
├── models/
│   ├── custom_feature_model.pkl     # Trained ML model
│   └── custom_feature_names.pkl     # List of feature names
├── data/
│   ├── phishing_dataset.csv         # Dataset with labels
├── logs/
│   └── results.log           # Log of scanned URLs
└── requirements.txt
```

---

## 🧠 How It Works

### 🔹 Rule-Based Detection

The `rule_based.py` module checks URLs for:

* `@` symbol
* Excessive hyphens
* IP address in place of domain
* Suspicious keywords (`login`, `verify`, `secure`, etc.)
* Underscores (e.g. `http://secure_login.com`)

### 🔹 ML-Based Detection

* URLs are converted to features (like length, digit count, etc.)
* Trained using `RandomForestClassifier`
* Predictions: `phishing` or `legitimate`

### 🔹 Hybrid Detection

* First applies rules
* If safe, uses ML model as backup
* Reason for rule-based detection is returned for explanation

---

## 🧪 Sample Output

```
http://secure-login.example.com --> phishing (by rule-based: contains suspicious keyword)
https://google.com              --> legitimate
http://google_com              --> phishing (by rule-based: contains underscore)
```

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/phishing_detector_project.git
cd phishing_detector_project
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser.

---

## 📄 Dataset Format

A CSV file with the following structure:

```csv
url,label
http://paypal-login.example.com,phishing
https://google.com,legitimate
```

---

## 🧪 Model Training (Optional)

If you want to retrain the model:

```bash
python src/ml_custom_features.py
```

This will regenerate:

* `custom_feature_model.pkl`
* `custom_feature_names.pkl`

---

## ✅ Example Features Extracted

| Feature              | Description                      |
| -------------------- | -------------------------------- |
| url\_length          | Total length of the URL          |
| dot\_count           | Number of dots in URL            |
| at\_count            | Number of `@` symbols            |
| has\_ip              | Whether IP address is used       |
| suspicious\_keywords | Count of phishing-related words  |
| underscore\_count    | Number of underscores in the URL |

---

## 📌 Future Improvements

* Add VirusTotal API integration
* Real-time ML model updating
* Dashboard view with charts
* Export results as PDF or CSV
* Voice input (Web Speech API)

---

## 🙌 Credits

Developed by: **Your Name**
Project Mentored and Guided by: **ChatGPT (AI Assistant)**

---

## 🛡️ Disclaimer

This tool is for **educational and research purposes only**. Do not rely solely on this model for real-world protection. Always consult professional security solutions.

---
