# Программа которая заменяет цифры числа 0 на 9, 1 на 8 и т.д.


num = int(input('input number='))
rez=''

while num:
    digit = num % 10
    rez = str(9 - digit) + rez
    num //= 10

print(rez)

