# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
import random
import string

letters = string.ascii_lowercase


def new_file(f_exten: str, min_len = 6, max_len = 30, min_b = 256, max_b = 4096, count = 42):
    for _ in range(count):
        name_len = random.randint(min_len, max_len)
        name = random.sample(letters, name_len)
        f_name = f'{"".join(name)}.{f_exten}'
        with open(f_name, 'wb') as f:
            f.write(bytes(random.randint(min_b, max_b)))
    return

new_file('txt', 3, 10, 256, 325, 2)