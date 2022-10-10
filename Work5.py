# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.



with open('file1.txt','r') as file:
    file1 = file.readline()
    list1 = file1.split()


with open('file2.txt','r') as file:
    file2 = file.readline()
    list2 = file2.split()

print(f'{list1} + {list2}')
sum = list1 + list2

with open('sum.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list1} + {list2}')
