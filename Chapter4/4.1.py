# Напишите программу в которой генерируется 15 случайных 
# целых чисел попадают в диапазон значений от 1 до 10 и 
# 10 случайных чисел попадают в диапазон от 10 до 30



from random import *

num1 = 3
num2 = 5

a = set()
b = set()
c = set()

while num1 > len(a):
    a.add(randint(1,10))

while num2 > len(b):
    b.add(randint(10,30))

c = a | b

print(a)
print(b)
print(c)