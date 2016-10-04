import vk
from my_data import MyVkData

session = vk.Session()
vkapi = vk.API(session)

friends = vkapi.friends.get(user_id=MyVkData.MY_USER_ID, fields='name')

friends_of_my_fiends = []
for friend in friends:
    user_id = friend['user_id']
    try:
        new_friends = vkapi.friends.get(user_id=user_id, fields='name')
    except vk.exceptions.VkAPIError as er:
        print(er)
    [friends_of_my_fiends.append(new_friend) for new_friend in new_friends]

print('Количество друзей у моих друзей %d \n'%(len(friends_of_my_fiends)))
[print(friend) for friend in friends_of_my_fiends[:10]]