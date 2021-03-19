import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='test'
result=requests.get(BASE_URL+ENDPOINT)
print(result.json())
print(type(result))
print('details coming from django application:')
print('name of the employee{}'.format(result.json()['name']))
