# Функция результат которой вовзращает сумму нечетных чисел. Количство
# числе передается аргументом.

up = int(input('input up limit='))

res = list(k for k in range(0,up))

n = 0
k = 0
while k < up:
    if n % 2 != 0:
        res[k] = int(n)
        k = k + 1
        n = n + 1    
    else:
        n = n + 1
    
def sum1(arg):
    print(arg)
    print(sum(arg))

sum1(res)
