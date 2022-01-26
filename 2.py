import pymysql
from hashlib import pbkdf2_hmac
from binascii import hexlify

try:
    connect = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='1111',
        database='lombard',
        cursorclass=pymysql.cursors.DictCursor
    )
    print('Connect is OK')
    print('*' * 30)

    try:

        def get_psw256(login, psw):
            obj = pbkdf2_hmac(hash_name='sha256', password=bytes(psw, encoding='utf-8'),
                              salt=bytes(login, encoding='utf-8'), iterations=100000)
            psw256 = str(hexlify(obj))
            return psw256


        login = input('Введите логин: ')
        psw = input('Введите пароль: ')

        with connect.cursor() as cur:
            cur.execute('DROP TABLE IF EXISTS test_au;')
            cur.execute('CREATE TABLE test_au (id SERIAL, login VARCHAR(50), password_hash VARCHAR(200));')
            cur.execute(f'INSERT INTO `test_au` VALUES (1, \'{login}\',\"{get_psw256(login, psw)}\");')
            connect.commit()

        print('*' * 20, 'Учетная запись создана', '*' * 20)

        login1 = input('Введите логин: ')
        psw1 = input('Введите пароль: ')

        with connect.cursor() as cur:
            select_psw = f'SELECT * FROM `test_au` WHERE login = \'{login1}\';'
            cur.execute(select_psw)
            rows = cur.fetchall()
            key = rows[0]['password_hash']

            if key == get_psw256(login1, psw1):
                print('Пароль верный')
            else:
                print('Пароль неверный')


    finally:
        connect.close()
except Exception as ex:
    print('Connection failed!')
    print(ex)
