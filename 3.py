import hashlib


def let_count(str):
    _set = {hashlib.sha1(str[i:j].encode('utf-8')).hexdigest() for i in range(len(str) + 1) for j in
            range(i + 1, len(str) + 1)}
    return print(_set)


let_count('good')

let_count('ok')
