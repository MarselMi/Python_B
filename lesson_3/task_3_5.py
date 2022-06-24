'''Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:

print(get_jokes(2))
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.

Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?'''
from random import random
from random import randint


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
    while count:
        world_1 = nouns[randint(0, len(nouns) - 1)]
        world_2 = adverbs[randint(0, len(adverbs) - 1)]
        world_3 = adjectives[randint(0, len(adjectives) - 1)]
        count -= 1
        list_out.append(f'{world_1} {world_2} {world_3}')
    return list_out


print(get_jokes(2))
print(get_jokes(10))


def get_jokes_adv(count: int, replay=True) -> list:

    jokes = zip(nouns, adverbs, adjectives)
    list_out = []
    for _ in range(0, count):
        list_out.append(next(jokes))
    return list_out

print(get_jokes_adv(3))