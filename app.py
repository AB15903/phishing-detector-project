# Flask: Framework to create web routes and handle HTTP requests.
# 
# render_template: Renders HTML files (from templates/ folder).
# 
# request: Handles form data (POST, GET, etc.).
# 
# redirect, url_for: Used to navigate between pages.
# 
# session: Temporarily stores data across requests (like url, result).
# 
# hybrid_predict: Your function that decides if a URL is phishing.
# 
# datetime: Used to timestamp scan logs.
# 
# log_scan_result: Utility function to write results to results.log.
# 
# os: Helps in creating directories (like logs/ if not already present).

from flask import Flask, render_template, request, redirect, url_for, session
from src.hybrid_detector import hybrid_predict
from datetime import datetime
from src.utils import log_scan_result
import os


# os.makedirs(...): Creates the logs/ directory if it doesn’t exist.
os.makedirs("logs", exist_ok=True)

# Flask(__name__): Creates a Flask application instance.
app = Flask(__name__)

# app.secret_key: Enables session usage. You must set a secret key to use sessions securely.
app.secret_key = "supersecret"          # required for session to work



# Route for the homepage (http://localhost:5000/).
@app.route('/')
def home():

    # Displays the form where the user enters a URL.
    return render_template('form.html')



# Triggered when user submits the form.
@app.route('/check', methods=['POST'])
def check():

    # Retrieves the URL from the form input.
    url = request.form['url']

    # Calls hybrid_predict(url) to analyze it
    result = hybrid_predict(url)

                                                                # ✅ Log the result to a file 
                                                                # with open("logs/results.log", "a") as log_file:
                                                                    # log_file.write(f"{datetime.now()} - {url} --> {result}\n")


  # Instead of writing manually to a file, you use a helper function log_scan_result() to save the detection result into logs/results.log.                                                                  
    log_scan_result(url, result)

    
    # Save result in session  temporarily and redirect

    # Stores the URL and result temporarily in Flask’s session.
    session['url'] = url
    session['result'] = result

    # Redirects to the /result route to display it.
    return redirect(url_for('result_page'))

    # return render_template('result.html', url=url, result=result)

# Retrieves URL and result from the session.
@app.route('/result')
def result_page():
    url = session.get('url')
    result = session.get('result')

    # Renders the result.html template with this data.
    return render_template('result.html', url=url, result=result)




@app.route('/history')
def history():
    entries = []
    try:
        with open("logs/results.log", "r") as file:
            for line in file:
                if '-->' in line:
                    timestamp_url, result = line.strip().split('-->')
                    timestamp, url = timestamp_url.split(' - ')
                    entries.append({
                        'timestamp':timestamp,
                        'url':url.strip(),
                        'result':result.strip()
                    })
    except FileNotFoundError:
        entries = []

    return render_template("history.html", entries=entries)           

#Reads the logs/results.log file line-by-line.
#Extracts:

        # timestamp → when the scan was made
        # url → what was scanned
        # result → phishing / legitimate
#Collects all results in a list entries and sends them to history.html.




if __name__ == '__main__':
    app.run(debug=True)

# This makes the app run locally at http://127.0.0.1:5000/.
# debug=True allows auto-reload when code changes and gives detailed error pages.

