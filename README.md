# 🏦 AI Loan Approval Prediction System

An end-to-end Machine Learning project that predicts whether a loan application will be approved based on applicant details. This project demonstrates data preprocessing, feature engineering, model training, and deployment using Streamlit.

---

## 🚀 Project Overview

This system uses a trained machine learning model to evaluate loan applications and predict approval probability.

The goal is to:

* Automate loan decision support
* Reduce manual risk evaluation
* Provide real-time predictions via a web interface

---

## 🧠 Features

* 📊 Machine Learning-based prediction
* 🧾 Handles categorical + numerical data
* 🔁 One-hot encoded feature system
* 🌐 Interactive UI using Streamlit
* 📈 Probability-based output (not just yes/no)

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* Pickle (model serialization)
* Streamlit (deployment)

---

## 📂 Project Structure

```
├── app.py                # Streamlit web app
├── model.pkl            # Trained ML model
├── model.py             # CLI-based prediction script
├── loan_detection.csv   # Dataset
├── features.pkl         # Feature list (if used)
├── project.ipynb        # Training & experimentation notebook
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
https://github.com/Maganpreet-11/credit-risk-model.git
```

### 2. Run the app

```
streamlit run app.py
```

---

## 📊 Model Details

* Algorithm: (Add yours here, e.g. Logistic Regression / Random Forest)
* Accuracy: ~70%
* Input Features:

  * Age
  * Job
  * Marital Status
  * Education
  * Loan history
  * Contact details
  * Campaign data
  * Previous outcomes

---

## 📌 How It Works

1. User enters details in the UI
2. Inputs are converted into model-compatible format
3. Features are aligned with trained model
4. Prediction is generated
5. Probability score is displayed

---

## ⚠️ Current Limitations

* Manual feature encoding (can cause inconsistencies)
* Limited feature engineering
* Accuracy can be improved with better preprocessing
* Not yet production-optimized

---

## 🔮 Future Improvements

* ✅ Replace manual encoding with ML pipeline
* ✅ Use advanced models (XGBoost / LightGBM)
* ✅ Handle class imbalance (SMOTE)
* ✅ Add feature importance visualization
* ✅ Deploy on cloud (AWS / Render / Hugging Face)

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Maganpreet Singh**
B.Tech CSE Student | Future AI Engineer 🚀

---

## ⭐ Final Note

This project is a strong foundation for building real-world fintech AI systems. With improved data handling and model optimization, it can evolve into a production-grade solution.

---
