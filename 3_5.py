import random

def get_jokes(quntity_jokes, flag=True):
    """Функция случайного выбора значений из списка

    Два параметра
    Количество шуток - тип число
    флаг повтора - тип Boolean

    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом", "барабан"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    i = 0
    if flag:
        while i < quntity_jokes:
            ran_nouns = random.choice(nouns)
            nouns.remove(ran_nouns)
            ran_adverbs = random.choice(adverbs)
            adverbs.remove(ran_adverbs)
            ran_adjectives = random.choice(adjectives)
            adjectives.remove(ran_adjectives)
            i = i + 1
            print(f'{i}) {ran_nouns} {ran_adverbs} {ran_adjectives}')
    else:
        while i < quntity_jokes:
            ran_nouns = random.choice(nouns)
            ran_adverbs = random.choice(adverbs)
            ran_adjectives = random.choice(adjectives)
            i = i + 1
            print(f'{i}) {ran_nouns} {ran_adverbs} {ran_adjectives}')


s = int(input('Введите количество шуток: '))
s2 = input('Повторять слова в шутках (0 - не повторять, 1 - повторять): ')
if s2 == "1":
    s2 = False
get_jokes(s, s2)
