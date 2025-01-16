import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

# App title and description
st.set_page_config(page_title="SMS Spam Detection", page_icon="📩", layout="centered")
st.title("📩 SMS Spam Detection")
st.write("""
This **Machine Learning** application detects SMS messages as **Spam** or **Ham** (Not Spam). 
Enter your SMS below and let the model do its magic! 🚀
""")

# Sidebar for additional information
st.sidebar.title("About Spam Detection")
st.sidebar.write("""
- **Spam**: Unwanted or unsolicited messages, often advertising or fraudulent.
- **Ham**: Genuine and desired messages.
- Our model uses **Machine Learning** techniques to differentiate between the two.
""")
st.sidebar.write("---")
st.sidebar.write("🔗 Learn more about [Spam Detection](https://en.wikipedia.org/wiki/Email_spam)")

# Input area for user SMS
st.subheader("Enter an SMS to detect")
user_input = st.text_area("✍️ Type your SMS here:", height=150, placeholder="Type something like 'Congratulations! You’ve won a prize! Claim now.'")

# Add button and classification logic
if st.button("🚀 Detect SMS"):
    if user_input.strip():
        # Preprocessing and prediction
        data = [user_input]
        vectorized_data = cv.transform(data).toarray()
        result = model.predict(vectorized_data)

        # Display results with visuals
        if result[0] == 0:
            st.success("✅ This SMS is **Not Spam** (Ham).")
            st.markdown("""
                **What is Ham?**
                - Genuine messages sent by people you know or from legitimate sources.
                """)
        else:
            st.error("🚨 This SMS is **Spam**.")
            st.markdown("""
                **What is Spam?**
                - Unsolicited messages, often sent in bulk.
                - Commonly used for advertising, phishing, or fraud.
                """)
    else:
        st.warning("⚠️ Please enter an SMS to detect!")

# Footer section with additional styling
st.write("---")
st.markdown("""
<div style="text-align: center; color: gray; font-size: 14px;">
    Built with ❤️ using Streamlit | © 2025 Preeti Gupta
</div>
""", unsafe_allow_html=True)
