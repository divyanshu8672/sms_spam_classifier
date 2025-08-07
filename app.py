
import streamlit as st
import pickle

# Load the saved model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# App title
st.title("📩 SMS Spam Detector")
st.write("Enter an SMS message below to classify it as Spam or Not Spam.")

# Input box for user text
input_sms = st.text_area("Enter SMS text here:")

# Predict button
if st.button("Predict"):
    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message to predict.")
    else:
        # Vectorize input text
        transformed_input = vectorizer.transform([input_sms])

        # Make prediction
        result = model.predict(transformed_input)[0]

        # Display result
        if result == 1:
            st.error("🚫 This message is SPAM")
        else:
            st.success("✅ This message is NOT spam")
