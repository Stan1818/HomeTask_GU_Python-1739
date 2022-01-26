import hashlib

cash = {'7efe10f9ea80a23354da1870d99e86fd4bc8047d340b872a240c941c6349896e': 'www.mail.ru'}

def ch_url(url):
    hash_u = hashlib.sha256(url.encode()).hexdigest()
    if hash_u in cash.keys():
        return print(cash)
    else:
        cash[hash_u] = url
        return print(cash)




try:
    cash.update(ch_url('www.mail1.ru'))
except TypeError:
    print("Такой кэш уже существует")
