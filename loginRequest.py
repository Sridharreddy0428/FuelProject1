import requests,json

url = "https://tspvahan.tspolice.gov.in/api/auto-fuel/v1/login"

payload = {'emp_id': '4501619',
'password': '123456'}
files=[

]
headers = {}
  
response = requests.request("POST", url, headers=headers, data=payload, files=files)

data=(json.loads(response.text))
print(type(data['statusCode']))
print(type(data['message']))
print(data['response']['token'])



