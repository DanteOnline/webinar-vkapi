import vk
from my_data import MyVkData

INTEREST_LIST = ['Художник','Игры','Туризм','Романтика']

SEX = 2 #1-женщина, 2-мужчина, 0-любой (по умолчанию)
AGE_FROM = 30
AGE_TO = 35
HAS_PHOTO = True
CITY_ID = 1 #Москва

session = vk.AuthSession(app_id=MyVkData.APP_ID, user_login=MyVkData.LOGIN, user_password=MyVkData.GET_PASSWORD())
vkapi = vk.API(session)

users = vkapi.users.search(interests=','.join(INTEREST_LIST), sex=SEX, age_from=AGE_FROM, age_to=AGE_TO, fields='photo_big,domain,bdate')

users_count = users[0]
print('Количество найденных половинок: %d'%(users_count))
users=users[1:]
[print(user) for user in users]
