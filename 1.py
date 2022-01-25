import time


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print(f'Время выполнения функции {f.__name__} = {time2 - time1}')
        return ret

    return wrap


# O(n)
@timing
def add_list(n):
    lst = [i for i in range(n)]  # O(n)
    return lst  # O(1)


test_list = add_list(1000000)


# O(n)
@timing
def add_dict(n):
    dct = {i: i for i in range(n)}  # O(n)
    return dct  # O(1)


test_dict = add_dict(1000000)

# O(1)
@timing
def edit_list(lst, j):
    lst[j] = 'test'  # O(1)
    return lst # O(1)


edit_list(test_list, 999999)

# O(1)
@timing
def edit_dict(dct, j, i):
    dct[i] = j# O(1)
    return dct# O(1)


edit_dict(test_dict, 342, 555)

#O(n)
@timing
def delete_list(lst, i):
    lst.pop(i) #O(n)
    return lst #O(1)


delete_list(test_list, 555)

#O(1)
@timing
def delete_dict(dct, i):
    del dct[i] #O(1)
    return dct #O(1)

delete_dict(test_dict, 555)
