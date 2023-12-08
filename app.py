import requests

PORT = 8000
WAIT_NORMAL = 0.5
WAIT_TIMEOUT = 2

def send_post(path: str, json):
    response = requests.post(f"http://localhost:{PORT}/api/{path}/", json=json)
    return response

def send_get(path: str):
    response = requests.get(f"http://localhost:{PORT}/api/{path}")
    return response.json()[-1]