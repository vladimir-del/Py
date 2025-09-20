# Напишите программу которая создает вложенный список. Размеры списка указываются 
# аргументами функции. Список заполняется случайныи буквами. 

from random import *

def show(kort):
    for i in kort:
        for j in i:
            print(j,' ',end='')
        print()


def mass(a,b):
    res = [[chr(randint(0,950)) for i in range(a)] for j in range(b)]
    return res

a = mass(2,3)

show(a)