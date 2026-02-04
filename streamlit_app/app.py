import streamlit as st
import pickle
import re

# -----------------------------
# Load model and vectorizer
# -----------------------------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# -----------------------------
# Text cleaning (optional but recommended)
# Use SAME logic as training
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z]", " ", text)
    return text

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="SMS Spam Classifier", layout="centered")

st.title("📩 SMS Spam Classifier")
st.write("Enter an SMS message to check whether it is **Spam** or **Not Spam**.")

sms_input = st.text_area("✉️ Enter SMS text here:")

if st.button("🔍 Predict"):
    if sms_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        cleaned_sms = clean_text(sms_input)
        vectorized_sms = vectorizer.transform([cleaned_sms])
        prediction = model.predict(vectorized_sms)[0]

        if prediction == 1 or prediction == "spam":
            st.error("🚨 This message is **SPAM**")
        else:
            st.success("✅ This message is **NOT SPAM**")
