# Задана последовательность натуральных чисел, завершающаяся числом 0. Требуется определить 
# значение второго по величине элемента в этой последовательности, то есть элемента, 
# который будет наибольшим, если из последовательности удалить наибольший элемент.
# Пример:
# 1 7 9 0 -> 7

from random import randint


n = int(input('Введите количество чисел в последовательности: '))
numbers = list()
for i in range(n-1):
    numbers.append(randint(1, 99))
numbers.append(0)

if numbers[0] > numbers[1]:
    max1 = numbers[0]
    max2 = numbers[1]
else:
    max1 = numbers[1]
    max2 = numbers[0]
for j in range(2, n):
    if numbers[j] > max1:
        max2 = max1
        max1 = numbers[j]
    if numbers[j] < max1 and numbers[j] > max2:
        max2 = numbers[j]
print('Заданная последовательность натуральных чисел:\n', numbers)
print('Второй по величине элемент последовательности:', max2)
           