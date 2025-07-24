# 📩 SMS Spam Detection Web App

A simple and interactive **Machine Learning web application** that detects whether an SMS message is **Spam** (unwanted/fraudulent) or **Ham** (genuine). Built using Python, Scikit-learn, and Streamlit.

---

## 🔍 About the Project

This project uses a trained Machine Learning model to classify SMS messages. It provides a user-friendly interface for live testing of text input.

- **Spam**: Unwanted or fraudulent messages (e.g., ads, scams).
- **Ham**: Genuine personal or business messages.
  
Model trained on a labeled SMS dataset and deployed locally using Streamlit.

---

## 🧠 Technologies Used

- **Python 3.10+**
- **Scikit-learn**
- **Pandas**
- **Streamlit**
- **Jupyter / VSCode** (optional for editing)

---

## 🚀 How to Run the App Locally

Follow these easy steps:

### ✅ Prerequisites

Make sure you have Python and pip installed:

```bash
python --version
pip --version

📁 1. Clone the Repository or Download Files
If using Git:

bash
Copy
Edit
git clone https://github.com/your-username/sms-spam-detector.git
cd sms-spam-detector
Or download the .zip and extract it.

📦 2. Install Required Packages
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
Linux/macOS:

bash
Copy
Edit
source venv/bin/activate
Windows:

bash
Copy
Edit
venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not present, install manually:

bash
Copy
Edit
pip install streamlit scikit-learn pandas
▶️ 3. Run the Streamlit App
Run the following command:

bash
Copy
Edit
streamlit run app.py
Then open your browser and go to:

arduino
Copy
Edit
http://localhost:8501
💡 Sample Inputs
✅ Ham (Not Spam)
"Hey, are we still meeting for lunch at 1 PM?"

❌ Spam
"Congratulations! You’ve won a free iPhone. Click here to claim your prize: http://scam.link/win123"

📸 Demo Screenshots
✅ Ham Message Result
<img width="600" alt="Ham Message Result" src="Screenshot 2025-07-24 195438.png" />

❌ Spam Message Result
<img width="600" alt="Spam Message Result" src="Screenshot 2025-07-24 195510.png" />

📁 Project Structure
bash
Copy
Edit
├── app.py                  # Streamlit App
├── model.pkl               # Trained ML model
├── vectorizer.pkl          # Fitted Tfidf Vectorizer
├── README.md               # Project Documentation
├── requirements.txt        # Python dependencies
✍️ Author
Preeti Gupta