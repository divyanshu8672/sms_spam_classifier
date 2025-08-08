
import streamlit as st
import pickle

# Load the trained model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Streamlit UI
st.title("📩 SMS Spam Classifier")
st.write("Enter a message below to check whether it is **Spam** or **Not Spam**.")

# Input box
user_input = st.text_area("✉️ Type your message here:")

# Prediction
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message before predicting.")
    else:
        # Transform input using vectorizer
        transformed_input = vectorizer.transform([user_input])

        # Predict using the model
        prediction = model.predict(transformed_input)[0]

        # Output result
        if prediction == 1:
            st.error("🚫 Spam message detected!")
        else:
            st.success("✅ This is NOT a spam message.")
