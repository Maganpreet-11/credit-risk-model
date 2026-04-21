# 🏦 AI Loan Approval Prediction System  

An end-to-end **Machine Learning project** that predicts whether a loan application will be approved based on applicant details.  
This project demonstrates **data preprocessing, feature engineering, model comparison, and deployment using Streamlit**.

---

## 🚀 Project Overview  

This system uses a trained ML model to evaluate loan applications and predict approval probability in real time.

### 🎯 Objectives:
- Automate loan decision support  
- Reduce manual risk evaluation  
- Provide real-time predictions via a web interface  

---

## 🧠 Features  

- 📊 Machine Learning-based prediction  
- 🧾 Handles categorical + numerical data  
- 🔁 One-hot encoded feature system  
- 🌐 Interactive UI using Streamlit  
- 📈 Probability-based output (not just yes/no)  
- ⚙️ Feature alignment with trained model (prevents mismatch errors)  

---

## 🛠️ Tech Stack  

- **Language:** Python 🐍  
- **Libraries:**  
  - Pandas  
  - NumPy  
  - Scikit-learn  
- **Model Storage:** Pickle  
- **Deployment:** Streamlit  

---

## 📂 Project Structure  
- ├── app.py # Streamlit web app
- ├── model.pkl # Trained ML model
- ├── model.py # CLI-based prediction script
- ├── loan_detection.csv # Dataset
- ├── features.pkl # Feature list
- ├── project.ipynb # Training & experimentation notebook
- ├── requirement.txt # Dependencies

---

## 📊 Model Details  

### Models Tested:
- Logistic Regression  
- Decision Tree  
- Random Forest ✅ (Selected)  

### Final Model:
- Random Forest  

### Accuracy:
- ~70%  

### Why Random Forest?
- Handles non-linear relationships  
- Reduces overfitting compared to Decision Trees  
- Performs well on real-world noisy data  

---

## 📌 How It Works  

1. User enters details in the UI  
2. Inputs are converted into model-compatible format  
3. One-hot encoding is applied  
4. Features are aligned with trained model  
5. Prediction is generated  
6. Probability score is displayed  

---

## 📸 Screenshots  

_Add your images here:_  
- Model Accuracy Comparison  
- Streamlit UI (Approved & Rejected cases)  
- Feature Importance Graph  

---

## ⚠️ Challenges Faced  

- Handling messy and inconsistent real-world data  
- Encoding categorical variables correctly  
- Ensuring feature alignment between training & prediction  
- Managing feature mismatch issues  

---

## ⚠️ Current Limitations  

- Manual feature encoding (can cause inconsistencies)  
- Limited feature engineering  
- Moderate accuracy (~70%)  
- Not yet production-optimized  

---

## 🔮 Future Improvements  

- Replace manual encoding with ML pipeline  
- Hyperparameter tuning (GridSearchCV)  
- Use advanced models (XGBoost / LightGBM)  
- Handle class imbalance (SMOTE / class_weight)  
- Add feature importance visualization in UI  
- Deploy on cloud (AWS / Render / Hugging Face)  

---

## 🎯 Key Learning  

> “In Machine Learning, data preparation matters more than model complexity.”

This project highlights:

- Importance of clean data  
- Feature engineering impact  
- Model comparison before selection  

---

## 🤝 Contributing  

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License  

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author  

**Maganpreet Singh**  
B.Tech CSE Student | Aspiring AI Engineer 🚀  

---

## ⭐ Final Note  

This project is a strong foundation for real-world fintech AI systems.  
With better data handling and optimization, it can evolve into a production-grade intelligent decision system.
