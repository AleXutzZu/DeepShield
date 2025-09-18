import requests

url = "http://localhost:8000/detect-deepfake/"

# Send local file
with open("images/test1.png", "rb") as f:
    response = requests.post(url, files={"file": f})

print(response.json())
