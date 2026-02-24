import requests

url = "http://localhost:8000/predict"
file = {'file': open('doggy.jpg', "rb")}
response = requests.post(url=url, files=file)
print(response.json())
