import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

import os

BASE_DIR = Path(__file__).resolve().parent.parent  # Goes from app/ → eduinsight/
model_path = BASE_DIR / "models" / "performance_model.pkl"
scaler_path = BASE_DIR / "models" / "scaler.pkl"


model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Title
st.set_page_config(page_title="EduInsight", layout="centered")
st.title("📊 EduInsight - Student Performance Predictor")
st.markdown("Predict student performance using ML based on their academic data.")

# Input form
# Input form
st.header("🧾 Manual Entry")

avg_quiz_score = st.number_input("Average Quiz Score", min_value=0.0, max_value=10.0, step=0.1)
attendance_pct = st.number_input("Attendance Percentage", min_value=0, max_value=100, step=1)
lms_interactions = st.number_input("LMS Interactions", min_value=0, step=1)
num_assignments = st.number_input("Assignments Submitted", min_value=0, step=1)

input_data = pd.DataFrame([{
    "avg_quiz_score": avg_quiz_score,
    "attendance_pct": attendance_pct,
    "lms_interactions": lms_interactions,
    "num_assignments_submitted": num_assignments
}])

# Force correct column order for scaler
expected_features = ['avg_quiz_score', 'attendance_pct', 'lms_interactions', 'num_assignments_submitted']
input_data = input_data[expected_features]

if st.button("🔮 Predict"):
    scaled_input = scaler.transform(input_data.to_numpy())
    prediction = model.predict(scaled_input)

    label_map = {
        0: "🚨 At Risk",
        1: "🟡 Average",
        2: "🌟 High Performer"
    }
    st.success(f"🎯 Predicted Label: {label_map[int(prediction[0])]}")

# 📂 CSV Upload
st.header("📂 Upload CSV for Bulk Prediction")
csv_file = st.file_uploader("Upload CSV file with required features", type=["csv"])

if csv_file is not None:
    try:
        data = pd.read_csv(csv_file)

        # ✅ Define correct column order expected by model
        expected_features = [
            "avg_quiz_score",
            "attendance_pct",
            "lms_interactions",
            "num_assignments_submitted"
        ]

        # ✅ Check if all required columns are present
        missing_cols = [col for col in expected_features if col not in data.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")

        # ✅ Reorder & convert to numpy for scaler
        data = data[expected_features]
        scaled = scaler.transform(data.to_numpy())
        preds = model.predict(scaled)

        # ✅ Add readable labels
        label_map = {0: "⚠️ At Risk", 1: "🟡 Average", 2: "✅ High Performer"}
        data["prediction"] = preds
        data["performance_label"] = data["prediction"].map(label_map)

        # ✅ Show result
        st.success("🎯 Prediction completed!")
        st.dataframe(data)

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
