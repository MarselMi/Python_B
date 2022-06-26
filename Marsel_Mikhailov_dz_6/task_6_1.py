'''Не используя библиотеки для парсинга, распарсить (получить определённые данные)
файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.'''


import requests


URL = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
urls = URL.text.split('\n')


def pars(urls: list):
    for info in urls:
        remote_addr = info[:info.find(' ')]
        request_type = info[info.find('"') + 1:info.find(' /downloads')]
        requested_resource = info[info.find('/downloads'):info.find(' HTTP')]
        yield (remote_addr, request_type, requested_resource)


gen = pars(urls)
for _ in range(1, len(urls)):
    print(next(gen))
