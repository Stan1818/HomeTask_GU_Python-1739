import time


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print(f'Время выполнения функции {f.__name__} = {time2 - time1}')
        return ret

    return wrap


@timing
def add_list(n):
    lst = [i for i in range(n)]
    return lst


test_list = add_list(1000000)


@timing
def add_dict(n):
    d = {i: i for i in range(n)}
    return d


test_dict = add_dict(1000000)


@timing
def edit_list(lst, j):
    lst[j] = 'test'
    return lst


edit_list(test_list, 999999)


@timing
def edit_dict(dct, j, i):
    dct[i] = j
    return dct


edit_dict(test_dict, 342, 555)
