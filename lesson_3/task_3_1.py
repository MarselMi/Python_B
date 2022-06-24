'''Написать функцию num_translate(), переводящую числительные от 0 до 10
c английского на русский язык.

Например:
    num_translate("one")
    "один"
    num_translate("eight")
    "восемь"
Если перевод сделать невозможно, вернуть None.

Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.'''

dictionary = {'one': 'один',
              'two': 'два',
              'three': 'три',
              'four': 'четыре',
              'five': 'пять',
              'six': 'шесть',
              'seven': 'семь',
              'eight': 'восемь',
              'nine': 'девять',
              'ten': 'десять'}


def num_translate(value: str):
    """переводит числительное с английского на русский """
    str_out = dictionary.get(value)
    return str_out


print(num_translate("one"))
print(num_translate("eight"))