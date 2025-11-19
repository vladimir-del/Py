# Напишите программу с функцией, аргументом которой передается 
# числовой список, а результатом является еще один список, в который 
# включены только нечетные числа из списка-аргумента.

a = [1,2,3,4,5,6,7,8,9]


def func(a):
    result = []
    for i in range(len(a)):
        if a[i] % 2 != 0:
            result.append(a[i])

    return result

print(func(a))
b = func(a)


for i in range(len(b)):
    print(b[i], b[i], sep='//', end='--')