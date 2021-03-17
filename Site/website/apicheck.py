import requests
BASE_URL='http://127.0.0.1:8000/'
CHECKPOINT='list'
result=requests.get(BASE_URL+CHECKPOINT)
print(result.json())