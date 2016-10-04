import vk
from my_data import MyVkData

session = vk.AuthSession(app_id=MyVkData.APP_ID, user_login=MyVkData.LOGIN, user_password=MyVkData.GET_PASSWORD())
vkapi = vk.API(session)

groups = vkapi.groups.search(q='Хакер', count=30)

groups_count = groups[0]
print('%d групп с темой Хакер'%(groups_count))
groups=groups[0]
[print(group) for group in groups]
