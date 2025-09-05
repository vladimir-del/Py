# Программа в которой пользователь вводаит целое число в программа,
# определяет сколько в этом чсиле цифр 0, 1, 2 или 9


num = input('input number=')
print(len(num))


num = int(input('input number='))
k = 0
while num >= 1:
    num = num // 10
    k = k+1
print('Digit =', k)