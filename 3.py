def let_count(sub_str):
    _set = {sub_str[i:j] for i in range(len(sub_str) + 1) for j in
            range(i + 1, len(sub_str) + 1)}
    return print(_set)


let_count('good')

let_count('ok')
