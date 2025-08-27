from hybrid_detector import hybrid_predict


# Sample URLs to test
urls = [
    "http://secure-login.example.com",
    "https://google.com",
    "http://update-facebook-info-alert.com",
    "https://apple.com",
    "http://login-verification-paypal.com"
    # "http://google_com"
]

for url in urls:
    result = hybrid_predict(url)
    print(f"{url} --> {result}")

