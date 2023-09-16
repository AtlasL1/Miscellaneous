import requests
url = "Insert link here"
response = requests.get(link)
print(response.status_code)
print(response.text)
