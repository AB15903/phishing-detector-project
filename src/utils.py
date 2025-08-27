from datetime import datetime
import os


def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")




def log_scan_result(url, result, path="logs/results.log"):
    """Append a scan result to the log file with timestamp."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as log_file:
        log_file.write(f"{get_current_timestamp()} - {url} --> {result}\n")



# Optional: reusable result formatter

def format_result_output(url, result):
    return f"{get_current_timestamp()} | {url} => {result}"

# Future utilities can go here
# def generate_pdf(...)
# def virus_total_lookup(...)
# def clean_url_text(...)