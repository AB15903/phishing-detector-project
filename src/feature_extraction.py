import re
 

def extract_features(url):
 features = {}

 # 1. URL length
 features['url_length'] = len(url)

 # 2. Count of '.'
 features['dot_count'] = url.count('.')

 # 3. Count of '-'
 features['hyphen_count'] = url.count('-')

 # 4. Count of digits
 features['digits_count'] = sum(c.isdigit() for c in url)

 # 5. Count of '@'
 features['at_count'] = url.count('@')

 # 6. Count of '//'
 features['double_slash_count'] = url.count('//') - 1   # subtract 'https://'

 # 7. Suspicious keywords
 suspicious_keywords = ['login', 'verify', 'account', 'update', 'secure', 'webscr']
 features['suspicious_keywords'] = sum(1 for word in suspicious_keywords if word in url.lower())

 # 8. Starts with https?
 features['https'] = 1 if url.lower().startswith('https://') else 0

 # 9. Underscore presence
 features['underscore_count'] = url.count('_')

 # 10. Uses IP instead of domain
 features['has_ip'] = int(bool(re.match(r'http[s]?://\d{1,3}(\.\d{1,3}){3}', url)))

 # 11.  Suspicious TLD
 suspicious_tlds = ['.zip', '.tk', '.xyz', '.info', '.top']
 features['suspicious_tld'] = int(any(url.endswith(tld) for tld in suspicious_tlds))


 return features