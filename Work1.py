# 1 Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10-1 <= d <= 10-10

from math import pi
import math

d = float(input('Введи число: '))
f = 0

while d != 1:
    d *= 10
    f += 1
print(f'Число π с заданной точностью = {round(pi,f)}')
    

