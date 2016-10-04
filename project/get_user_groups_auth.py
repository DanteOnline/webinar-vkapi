import vk
from my_data import MyVkData

session = vk.AuthSession(app_id=MyVkData.APP_ID, user_login=MyVkData.LOGIN, user_password=MyVkData.GET_PASSWORD())
vkapi = vk.API(session)

groups = vkapi.groups.get(user_id=MyVkData.DUROV_USER_ID, extended=1)

groups_count = groups[0]
print('Павел Дуров состоит в %d группах \n'%(groups_count))
groups = groups[:1]
[print(group) for group in groups]