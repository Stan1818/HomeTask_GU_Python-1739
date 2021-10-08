from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        lst = [el for el in (*args, *kwargs.values())]
        n = [f"{func.__name__}({el} --- {type(el)})" for el in lst]
        print(n)
        print(*n, *func(*args, **kwargs), sep=",\n")

    return wrapper


@type_logger
def calc_cube(*x, **y):
    num_list = [el for el in (*x, *y.values()) if isinstance(el, int) or isinstance(el, float)]
    return [i ** 3 for i in num_list]


a = calc_cube(1, 5, {'num': 3}, (2, 'name'), {8, 5}, [19, 3], 'str', firstname='Ivan')
print(a)
