# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

n = int(input("Введите первый элемент прогрессии: "))
k = int(input("Введите шаг последовательности: "))
m = int(input("Введите количество элементов в массиве: "))

for i in range(m):
    print(n + i * k, end=" ")


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)