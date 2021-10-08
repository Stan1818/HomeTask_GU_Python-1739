import re


def email_parse(mail):
    dct = {}
    pattern_login = r'(^[a-zA-Z0-9_\.+-]+)'
    pattern_domain = r'@[a-z0-9.-]+\.[a-z]+'
    try:
        dct.setdefault('username', re.match(pattern_login, mail).group())
        dct.setdefault('domain', re.search(pattern_domain, mail).group()[1:])
        return print(dct)
    except (ValueError, AttributeError) as e:
        print(f'Неверный формат {e}')


for i in ['stan987@g-ma.il.ru','stan@mail.ru','someone@geekbrains.ru', 'som&eone@geekbrainsru', 'someone@geekbrainsru']:
    try:
        email_parse(i)
    except ValueError as err:
        print(err)


