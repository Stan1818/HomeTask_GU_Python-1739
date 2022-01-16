users = {'ivan': ['fff', 1],
         'stan': ['sss', 0],
         'serj': ['aaa', 1]}


# O(1)
def access_user1(auth):
    user = input('Введите логин: ')
    passw = input('Введите пароль: ')
    if not auth.get(user):
        print('Нет такого пользователя')
    elif auth.get(user)[0] != passw:
        print('Неверный пароль')
    elif auth.get(user)[1] == 0:
        print('Активируйте учетную запись')
    else:
        print(f"Добро пожаловать {user}!")


# O(n)
def access_user2(auth):
    user = input('Введите логин: ')
    passw = input('Введите пароль: ')
    for key, value in auth.items():
        if key == user:
            if value[0] == passw and value[1] == 1:
                print(f"Добро пожаловать {user}!")
            elif value[0] == passw and value[1] == 0:
                print('Активируйте учетную запись')
            elif value[0] != passw:
                print('Неверный пароль')


access_user1(users)
access_user2(users)
