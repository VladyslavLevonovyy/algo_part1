import requests 
url = "https://www.netflix.com/ua/" 
response = requests.get(url)
print(response.text)





