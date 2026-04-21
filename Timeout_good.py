import requests

def fetch_data():
    url = "http://example.com/api/data"
    try:
        response = requests.get(url, timeout=5)  # ✅ Set timeout
        print("Status:", response.status_code)
        print("Data:", response.text)
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

fetch_data()
