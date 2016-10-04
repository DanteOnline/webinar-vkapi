import vk
from my_data import MyVkData

session = vk.AuthSession(app_id=MyVkData.APP_ID, user_login=MyVkData.LOGIN, user_password=MyVkData.GET_PASSWORD(), scope='wall')
vkapi = vk.API(session)

MESSAGE = 'Hello from Python Again'
vkapi.wall.post(message=MESSAGE)