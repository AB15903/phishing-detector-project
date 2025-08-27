# Imports is_suspicious() to run rule-based phishing checks.
from src.rule_based import is_suspicious  

# Imports extract_features() to convert URLs into machine-learning features.
from src.feature_extraction import extract_features  

 # joblib is used to load the trained ML model and features.
import joblib         

 # pandas is used for creating a DataFrame from feature vectors.
import pandas as pd                                            


# Load the trained ML model and features names

 # Loads the saved RandomForestClassifier model.
ml_model = joblib.load("models/custom_feature_model.pkl") 

# Loads the list of feature names used during training.
feature_names = joblib.load("models/custom_feature_names.pkl")  


# This function takes a URL and classifies it using rules first, then ML if needed.
def hybrid_predict(url):                                       

    # Step 1: Rule-based logic 
    # suspicious, reason = is_suspicious(url)       # -> for boolean 

    # Checks the URL with heuristics (e.g., suspicious keywords, hyphens, etc.).
    # If suspicious, it immediately returns a phishing verdict with the reason.
    suspicious, reason = is_suspicious(url, explain=True)          # -> for hybrid_predict 
    if suspicious:
        # return "phishing (by rule-based)"
        return f"phishing (by rule-based: {reason})"
    
    # Step 2: ML logic

    # Converts the URL into a feature vector (length, digits, keywords, etc.).
    # Creates a one-row DataFrame for prediction.
    features = extract_features(url)
    feature_vector = [features.get(name, 0) for name in feature_names]
    feature_df = pd.DataFrame([feature_vector], columns=feature_names)
    # prediction = ml_model.predict([features_vector])[0]

    # Uses the model to predict if the URL is phishing (1) or legitimate (0).
    prediction = ml_model.predict(feature_df)[0]


    # Based on ML prediction, returns the result as a string with source label.
    if prediction == 1:
        return "phishing (by ML)"
    else:
        return "legitimate"
    
# This runs the function on a test URL (in this case, "http://google_com") when the file is run directly.
if __name__ == "__main__":
    test_url = "http://secure-login.example.com"
    test_url = "http://google_com"
    result = hybrid_predict(test_url)
    
    # Prints out whether it is phishing or legitimate.
    print(f"{test_url} --> {result}")