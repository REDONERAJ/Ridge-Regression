## Insurance Charges Predictor - Ridge Regression
A Flask-based web application that predicts medical insurance charges based on age, BMI, children, smoker status, and region. Powered by Ridge Regression.

## Table of Contents
- Overview
- Features
- Tech Stack
- Installation
- Usage
- Project Structure
- Dataset
- Screenshots
- License

---

## Overview
This project uses **Ridge Regression** to estimate insurance costs for individuals based on demographic and health-related factors.  
It is designed for quick and reliable charge estimation using the publicly available Insurance dataset.

---

## Features
- Takes **5 user inputs**: Age, BMI, Children, Smoker status, and Region
- Predicts insurance charges in **USD**
- User-friendly UI with dropdowns for categorical fields
- Model trained on a real-world dataset
- Easy to run locally with Flask

---

## Project Structure
```
ridge-insurance-predictor/
│
├── app.py                       # Main Flask app
├── model.py                     # Model training script
├── ridge_insurance_model.pkl    # Saved regression model
├── smoker_encoder.pkl           # Saved encoder for smoker field
├── region_encoder.pkl           # Saved encoder for region field
├── templates/
│   └── index.html               # Frontend HTML
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## Tech Stack
| Technology     | Use |
|----------------|-----|
| Python         | Core language |
| Flask          | Web framework |
| scikit-learn   | ML modeling |
| HTML/CSS       | Frontend UI |
| Pandas         | Data handling |
| NumPy          | Numerical operations |
| Joblib         | Model persistence |

---

## Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/<your-username>/ridge-insurance-predictor.git
cd ridge-insurance-predictor
pip install -r requirements.txt
```

Train the model:
```bash
python model.py
```

Run the Flask server:
```bash
python app.py
```

Open your browser and go to:
```
http://127.0.0.1:5000/
```

---

## Dataset
**Source:** [Insurance Charges Dataset](https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv)

**Selected Features:**
- Age — Age of the individual
- BMI — Body Mass Index
- Children — Number of children covered by insurance
- Smoker — Whether the individual smokes (Yes/No)
- Region — Residential region (Southwest, Southeast, Northwest, Northeast)

**Target Variable:**
- Charges — Annual insurance charges in USD

---

## Screenshots
<img width="1366" height="633" alt="Screenshot 2025-08-10 183801" src="https://github.com/user-attachments/assets/54f53d2e-966b-45b9-bf2e-a0ec56a21f6d" />
<img width="1366" height="644" alt="Screenshot 2025-08-10 183842" src="https://github.com/user-attachments/assets/6092a879-9be4-4a4b-a81e-438a036a6694" />
<img width="1366" height="633" alt="Screenshot 2025-08-10 183853" src="https://github.com/user-attachments/assets/4509d874-dc1d-4f70-b605-45a13455be49" />



---
