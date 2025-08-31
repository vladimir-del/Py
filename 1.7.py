# Вычисление факториала. Ввод ползователем. Проверка на положительное число. 

num = int(input('input number='))

while num <= 0:
    print('Введите число больше нуля')
    num = int(input('input number='))

k = 1
res = 1

while k < num + 1:
    res = res * k
    k = k + 1

print('Факториал числа', num, 'равен=', res)