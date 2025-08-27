import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from feature_extraction import extract_features
import joblib

# pandas: For handling CSV data.
# RandomForestClassifier: A machine learning model that works well with tabular data.
# train_test_split: Used to split data into training and testing sets.
# accuracy_score: To evaluate model performance.
# extract_features: Custom function (you wrote earlier) that extracts features from each URL.
# joblib: Used to save/load models and Python objects efficiently.


# Step 1: Load dataset
df = pd.read_csv("data/ml_phishing_dataset.csv")
df = df.dropna()
df['label'] = df['label'].astype(str).str.strip().map({'phishing': 1, 'legitimate': 0})

# Step 2: Extract custom features
feature_dicts = df['url'].apply(extract_features)
features_df = pd.DataFrame(feature_dicts.tolist())

# Step 3: Train/test split
X_train, X_test, y_train, y_test = train_test_split(features_df, df['label'], test_size=0.2, random_state=42)

# Step 4: Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 5: Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Custom Feature-Based Accuracy: {acc * 100:.2f}%")

# Step 6: Save model
joblib.dump(model, "models/custom_feature_model.pkl")
joblib.dump(list(features_df.columns), "models/custom_feature_names.pkl")


