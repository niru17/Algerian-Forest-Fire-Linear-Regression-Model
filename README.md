# Algerian Forest Fire Linear Regression Model

This project implements an **end-to-end Machine Learning pipeline** to predict the **Fire Weather Index (FWI)** for the Algerian Forest Fire dataset. The project uses **Ridge Regression** for prediction and is deployed as a **Flask web application** with an HTML frontend.

---

## 📌 Project Overview
- **Dataset**: Algerian Forest Fire Dataset (UCI Machine Learning Repository)  
- **Target Variable**: Fire Weather Index (FWI) – a continuous float value  
- **Features**:  
  - Temperature  
  - Relative Humidity (RH)  
  - Wind Speed (Ws)  
  - Rain  
  - Fine Fuel Moisture Code (FFMC)  
  - Duff Moisture Code (DMC)  
  - Initial Spread Index (ISI)  
  - Classes  
  - Region  

- **ML Model**: Ridge Regression (trained & serialized using `pickle`)  
- **Deployment**: Flask backend with HTML frontend form  

---

## ⚙️ Tech Stack
- **Python** (Flask, Scikit-learn, Pandas, Numpy)  
- **Frontend**: HTML (Jinja templates)  
- **Modeling**: Ridge Regression with Standard Scaler  
- **Deployment**: Local Flask server  

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/niru17/Algerian-Forest-Fire-Linear-Regression-Model.git
cd Algerian-Forest-Fire-Linear-Regression-Model
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask app
```bash
python3 application.py
```

The app will start on 👉 `http://127.0.0.1:5000`

---

## 🖼️ Application Workflow

1. User opens the **web form** (`home.html`).  
2. Inputs values for features (Temperature, RH, Ws, Rain, etc.).  
3. Form submits data to Flask backend (`/prediction_data`).  
4. Backend scales the inputs → applies trained **Ridge model** → returns prediction.  
5. Prediction (FWI score) is displayed on the webpage.  

---

## 📂 Project Structure
```
.
├── application.py          # Flask app
├── models/
│   ├── ridge.pkl           # Trained Ridge Regression model
│   ├── scaler.pkl          # Standard Scaler
├── templates/
│   ├── index.html          # Landing page
│   ├── home.html           # Prediction form
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---
## 🌟 Future Improvements
- Deploy on **Heroku / AWS / Azure** for public access.  
- Add **classification model** for Fire/Not Fire prediction using `Classes`.  
- Build a **Bootstrap frontend** for better UI.  
---

## ✨ Author
**Niranjana Subramanian**  
📌 MS in Computer Science, University of Texas at Arlington 
