# Отображение чисел Фибоначчи. Ввод количества с клаваитуры. 

up = int(input('input up limit='))

while up <= 0:
    print('Введите число больше нуля')
    up = int(input('input number='))

k = 2
res = list(range(1,up))

res[0:1] = [1, 1]
while k < up:
    res[k] = res[k-1] + res[k-2]
    k=k+1
print(res)
