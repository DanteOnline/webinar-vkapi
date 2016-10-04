import vk
from my_data import MyVkData

session = vk.Session()
vkapi = vk.API(session)

friends = vkapi.friends.get(user_id=MyVkData.MY_USER_ID, fields='domain')

print('У меня %d друзей \n'%(len(friends)))
[print(friend) for friend in friends]

