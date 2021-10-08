import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        remote_addr = r'(([0-9]{1,3}[\.]){3}[0-9]{1,3})|([A-Z]{3,4})|(([\w]{1,4}[\:]){7}[\w]{1,4})'
        request_datetime = r'\d\d\/\w\w\w\/\d\d\d\d\:\d\d\:\d\d\:\d\d \+\d\d\d\d'
        request_type = r'[A-Z]{3}'
        requested_resource = r'[A-Z]{3} \/\w+\/\w+'
        response_code_size = r'\" \d+ \d+'
        code_size = re.search(response_code_size, line).group()[2:]
        code = code_size[:code_size.find(' ')]
        size = code_size[code_size.find(' ') + 1:]
        print(((re.search(remote_addr, line).group()), (re.search(request_datetime, line).group()),
               (re.search(request_type, line).group()), (re.search(requested_resource, line).group()[4:]), code, size))
