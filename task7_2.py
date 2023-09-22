# Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random as rnd
import string

ALHPA = string.ascii_lowercase
VOWELS = 'aeiouy'


def names_gen():
    min_len = 4
    max_len = 7
    name_len = rnd.randint(min_len,max_len)
    name = rnd.sample(ALHPA, name_len-1)
    name.append(rnd.choice(VOWELS))
    rnd.shuffle(name)
    return ''.join(name).title()


def name_file(count:int):
    with open('names.txt', 'w', encoding='UTF-8') as file:
        for _ in range(count):
            file.write(f'{names_gen()} \n')
    return

add_name_file(10)

