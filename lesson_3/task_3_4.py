'''*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую
в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
в котором ключи — первые буквы фамилий, а значения — словари, реализованные
по схеме предыдущего задания и содержащие записи, в которых фамилия начинается
с соответствующей буквы.

Например:
 thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Как поступить, если потребуется сортировка по ключам?'''


def thesaurus_adv(*args) -> dict:
    dict_out = {}
    for name_surname in args:
        name = name_surname.split(' ')[0]
        surname = name_surname.split(' ')[1]
        dict_out[surname[0]] = {name[0]: [name_surname]}
        if dict_out.get(surname[0]).get(name[0]) is not None:
            dict_out.get(surname[0]).get(name[0]).append(name_surname)
        else:
            dict_out.get(surname[0]).setdefault(name[0], name_surname)
    return dict_out


''' 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values' '''
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
