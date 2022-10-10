# 4 Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random


def create_file(x):
    with open('file.txt', 'w') as data:
        data.write(x)


k = int(input("Введите натуральную степень k = "))
lis = []
for i in range(k+1):
    lis.append(random.randint(0, 101))


def polynomial(x):
    lis = x[::-1]
    n = ''
    if len(lis) < 1:
        n = 'x = 0'
    else:
        for i in range(len(lis)):
            if i != len(lis) - 1 and lis[i] != 0 and i != len(lis) - 2:
                n += f'{lis[i]}x^{len(lis)-i-1}'
                if lis[i+1] != 0:
                    n += ' + '
            elif i == len(lis) - 2 and lis[i] != 0:
                n += f'{lis[i]}x'
                if lis[i+1] != 0:
                    n += ' + '
            elif i == len(lis) - 1 and lis[i] != 0:
                n += f'{lis[i]} = 0'
            elif i == len(lis) - 1 and lis[i] == 0:
                n += ' = 0'
    return n


create_file(polynomial(lis))
