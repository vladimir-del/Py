# Напишите программу, в которой описана функция. В качестве аргументов функции передаются два объекта одного и того же класса. 
# У каждого объекта есть поле, представляющее собой список из целых чисел. В результате функция возвращает объект того же класса. 
# Поле список этого объекта получается суммированием соответствующих элементов из полей-списков объектов, переданных аргументами функции. 
# Если в этих объектах списки разной длины, то недостающие элементы  в списке заменяются нулями.

import random as rd

class my:
    my_list=[x for x in range(8)]

A = my()
B = my()

A.list_A = [rd.randint(1,8) for x in range(rd.randint(1,5))]
B.list_B = [rd.randint(1,8) for x in range(rd.randint(1,5))]

def func(a , b):
    
    c = my()

    max_lengt = max(len(a.list_A), len(b.list_B))
    c.list_C = []

    for i in range(max_lengt):
        try:
            c.list_C.append(a.list_A[i] + b.list_B[i])
        except IndexError:
            c.list_C.append(0)
    return c

C = func(A, B)

print(C.__dict__)