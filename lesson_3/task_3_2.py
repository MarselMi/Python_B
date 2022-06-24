'''*(вместо задачи 1) Перепишите функцию из задания 1 изменив название на num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат
тоже должен быть с заглавной.
Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два" '''


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


def num_translate_adv(value: str):
    """переводит числительное с английского на русский """
    if value == value.title():
        str_out = dictionary.get(value.lower()).title()
    else:
        str_out = dictionary.get(value)
    return str_out


print(num_translate_adv("one"))
print(num_translate_adv("two"))
print(num_translate_adv("Eight"))