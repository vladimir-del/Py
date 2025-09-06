# Пользователь вводит список целочисленных значений, 
# а также верхнюю границу для вычисления суммы. 
# Программа вычисляет сумму натуральных чисел, за 
# исключением тех кто входит в список. 


seq = eval(input('Input except numbers= '))
up = int(input('Input up limit= '))

res = 0
k = 0

while k <= up:
    
    res = res + k
    k +=1
    
    for num in seq:
        if k == num:
            k +=1
            continue

print(res)