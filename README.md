# EduInsight – Student Performance Predictor

**EduInsight** is a real-time data science project that predicts student performance based on academic metrics like quiz scores, attendance, LMS interactions, and assignment submissions. This tool helps educators identify "At Risk" students early and plan personalized interventions.

---

##  Features

* Manual input prediction  
* CSV bulk upload prediction  
* ML-based classification: Logistic Regression, Random Forest, and XGBoost  
* Performance categories:  
- At Risk  
- Average  
- High Performer  
* Built with Streamlit for an interactive UI  
* Visualizations for performance trends (optional extension)

---

## ML Pipeline

- **Data Preprocessing**  
  - Missing value handling  
  - Feature engineering  
  - Scaling with `StandardScaler`

- **Model Training**  
  - Logistic Regression  
  - Random Forest  
  - XGBoost Classifier

- **Evaluation Metrics**  
  - Accuracy  
  - Confusion Matrix  
  - Classification Report (Precision, Recall, F1)

- **Model Output**  
  - Pickled `.pkl` models (`performance_model.pkl`, `scaler.pkl`)

---

##  Tech Stack

- **Languages & Libraries**: Python, NumPy, Pandas, Scikit-Learn, XGBoost, Seaborn, Matplotlib  
- **Deployment**: Streamlit  
- **Storage**: CSV  
- **Dev Tools**: VS Code, Jupyter Notebook, GitHub  

---


## Sample CSV Format for Bulk Upload

```csv
avg_quiz_score,attendance_pct,lms_interactions,num_assignments_submitted
6.5,80,12,8
4.2,65,5,4
8.1,92,18,9

```

## How to Run Locally
```bash
git clone https://github.com/yourusername/eduinsight.git
cd eduinsight
py -3.10 -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```
---

Deployed App
👉 https://eduinsight-4cjnwfk6dtvcnu3byslhpp.streamlit.app/

---
Author
Sudharshana J
B.E. CSE


