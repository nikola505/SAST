import requests

def fetch_data():
    url = "http://example.com/api/data"
    response = requests.get(url)  # ⚠️ No timeout set
    print("Status:", response.status_code)
    print("Data:", response.text)

fetch_data()
