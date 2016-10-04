import requests
from my_data import MyVkData

url = MyVkData.API_URL + 'users.get?user_ids=%s,%s'%(MyVkData.DUROV_USER_ID, MyVkData.MY_USER_ID)
print(url)

user_ids = MyVkData.DUROV_USER_ID+','+MyVkData.MY_USER_ID
response = requests.get(MyVkData.API_URL + 'users.get', {'user_ids':user_ids})
result = response.text
print(result)

import json
response_dict = json.loads(result)

users = response_dict['response']
[print(user) for user in users]






