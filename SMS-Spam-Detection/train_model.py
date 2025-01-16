import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load dataset
data = pd.read_csv("spam.csv", encoding='latin-1')
data = data.rename(columns={"v1": "label", "v2": "message"})[["label", "message"]]

# Map labels to binary values
data["label"] = data["label"].map({"ham": 0, "spam": 1})

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(data["message"], data["label"], test_size=0.2, random_state=42)

# Vectorize text data
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)

# Train model
model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

# Evaluate model
accuracy = model.score(vectorizer.transform(X_test), y_test)
print(f"Accuracy: {accuracy}")

# Save model and vectorizer
with open("spam_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)
with open("vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("Model and vectorizer saved successfully!")
