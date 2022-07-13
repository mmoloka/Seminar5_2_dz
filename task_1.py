# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
#    6782 -> 23
#    0,56 -> 11

num = float(input('Введите вещественное число: '))
num_str = str(num)
sum = 0
for i in range(len(num_str)):
    if num_str[i].isdigit():
        sum += int(num_str[i])
print('Сумма цифр числа = ', sum)
