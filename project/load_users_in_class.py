class VkUser:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_dict(cls, user_dict):
        first_name = user_dict['first_name']
        last_name = user_dict['last_name']
        return cls(first_name, last_name)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

if __name__ == '__main__':
    import vk
    from my_data import MyVkData

    # Создаем объект api
    vkapi = vk.API(vk.Session())
    # Получаем пользователей в виде словарей
    user_dicts = vkapi.users.get(user_ids=MyVkData.DUROV_USER_ID+','+MyVkData.MY_USER_ID+',49584683')
    # Создаем список для пользователей нашего класса
    users = []
    # Создаем пользователей из пользователей словарей
    [users.append(VkUser.from_dict(user_dict)) for user_dict in user_dicts]
    # Печатаем результат
    [print(user) for user in users]
