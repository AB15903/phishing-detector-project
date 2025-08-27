import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib





# Step 1: Load dataset
df = pd.read_csv("data/ml_phishing_dataset.csv")

df = df.dropna()            # Remove empty rows (optional)

# 🔧 Clean up labels (this is the fix)
# df['label'] = df['label'].str.strip()
df['label'] = df['label'].astype(str).str.strip().map({'phishing': 1, 'legitimate': 0})

# 🔁 Map labels to binary
# df['label'] = df['label'].map({'phishing': 1, 'legitimate': 0})

# 🧪 Optional check 
print("Labels after cleaning:", df['label'].unique())
print("Rows with NaN after mapping:\n", df[df['label'].isna()])

# Print unique labels
# print("Labels before mapping:", df['label'].unique())

# Step 2: Preprocess labels
# df['label'] = df['label'].map({'phishing': 1, 'legitimate': 0})

# 🔍 Check for NaN in y

# print("Labels after mapping (NaN check):")
# print(df[df['label'].isna()])

# Step 3: Feature Extraction from URL text (basic bag-of-words)
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(df['url'])

y = df['label']

# Step 4: Split into train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Step 5: Train model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Step 6: Evaluate
y_pred = model.predict(x_test)
acc = accuracy_score(y_test, y_pred)
print(f"ML-Based Detection Accuracy: {acc * 100:.2f}%")

# Step 7: Save model (optional)
joblib.dump(model, "models/phishing_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
