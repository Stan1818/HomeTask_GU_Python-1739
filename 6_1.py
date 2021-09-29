result = list()
spamer = []
dct = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for i in f:
        data = f.readline()
        remote_adr = data[0:data.find(' - - ')]
        request_type = data[data.find('+0000]') + 8:data.find('+0000]') + 11]
        requested_resource = data[data.find('+0000]') + 12:data.find('HTTP/') - 1]
        result.append((remote_adr, request_type, requested_resource))
        spamer.append(remote_adr)
for i in spamer:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1
for i in result:
    print(i)
print('*' * 50)
print('Спамер--->', max(dct.items(), key=lambda k: k[1]))
