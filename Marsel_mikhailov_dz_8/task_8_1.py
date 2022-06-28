'''Написать тело функцию email_parse(email: str), которая при помощи регулярного выражения
извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError. Пример:

$ email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
$ email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?'''


import re


def email_parse(email: str) -> dict:
    """
        Парсит переданную email-строку на атрибуты и возвращает словарь
        :param email: строковое входное значение обрабатываемого email
        :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
        """
    RE_MAIL = re.compile(r"^(?P<username>\w[\w!#$%&'*+/=?^_`{|}~-]*\w)@(?P<domain>\w[\w-]*\w\.\w+)$", re.IGNORECASE | re.ASCII)
    msg = f'wrong email: {email}'
    match_email = RE_MAIL.match(email)
    if not match_email:
        raise ValueError(msg)
    dict_out = match_email.groupdict()
    return dict_out


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    #email_parse('someone@geekbrainsru')