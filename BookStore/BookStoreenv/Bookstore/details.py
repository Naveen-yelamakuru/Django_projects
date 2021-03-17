import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='listdetails'
# def employee(id):

#     data=requests.get(BASE_URL+ENDPOINT+id)
#     print(data.status_code)
#     print(data.json())
# value=input('enter id:')

data=requests.get(BASE_URL+ENDPOINT)
# for i in data:
#     print(i)
print(data.status_code)
print(data.json())


