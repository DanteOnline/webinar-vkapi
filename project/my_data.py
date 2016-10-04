class MyVkData:
    # Идентификатор моего пользователя вконтакте
    MY_USER_ID = '273476094'
    # Идентификатор Павла Дурова
    DUROV_USER_ID = '1'
    # Общая ссылка для доступа к api
    API_URL = 'https://api.vk.com/method/'
    #Идентификатор приложения вконтакте
    APP_ID = 5455219
    #Логин пользователя ВКонтакет
    LOGIN = 'univer_gmail@rambler.ru'

    #Мой пароль вконтакте
    @staticmethod
    def GET_PASSWORD():
        f = open('/home/dante/pass.txt','r')
        passw = f.read().rstrip()
        f.close()
        return passw

if __name__ == '__main__':
    passw = MyVkData.GET_PASSWORD()
    #print(passw)
    #print('end')