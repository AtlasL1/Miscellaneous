import requests
url = "Insert link here"
response = requests.get(url)
print(response.status_code)
print(response.text)
