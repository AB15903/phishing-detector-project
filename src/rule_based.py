import re 
import pandas as pd


# Rule-based phishing detector
# def is_suspicious(url: str) -> bool:
def is_suspicious(url: str, explain=False) -> bool:
    """Detect if a URL is suspicious based on basic patterns."""
    # Rule 1: Has '@' symbol (used to trick users)
    if '@' in url:
        return (True, "contains '@'") if explain else True
    
    # Rule 2: Too many hyphens (often used in phishing)
    if url.count('-') > 3:
        return (True, "too many hyphens") if explain else True
    
    # Rule 3: Uses IP address instead of domain
    if re.match(r'http[s]?://\d{1,3}(\.\d{1,3}){3}',url):
        return True, ("uses IP address") if explain else True
    
    # Rule 4: Contains suspicious keywords
    suspicious_keywords = ['login','verify','update','secure','account','bank']
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        return True, ("contains suspicious keyword") if explain else True

    # Rule 5: Contains underscore(_) -common in spam/phishing domains
    if '_' in url :
        return True, ("contains underscore") if explain else True
    
    return (False, "") if explain else True 


# Evaluate rules on dataset
def evaluate_rule_based_model(csv_path: str):
    df = pd.read_csv(csv_path)
    df['predicted']=df['url'].apply(lambda x: 'phishing' if is_suspicious(x) else 'legitimate')


    accuracy = (df['label'] == df['predicted']).mean() * 100
    print(f"Rule-based Detection Accuracy: {accuracy:.2f}%")
    print(df[['url','label','predicted']])

# Run evaluation
if __name__ == "__main__":
    evaluate_rule_based_model("data/phishing_dataset.csv")