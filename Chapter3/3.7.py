# Напишите программу с функцией, которая для списка, 
# переданного аргументом, возвращает список из двух 
# элементов: значение наибольшего элемента в списке и 
# индекс этого элемента в списке (если таких элементов 
# несколько, то индекс первого из таких элементов).

from random import * 

def search(A):
    
    res = []
    MaxValue = max(A)
    IndxMaxValue = A.index(MaxValue)

    res = [MaxValue, IndxMaxValue]

    return res

a = [randint(0,9) for i in range(9)]

b = search(a)

print(a)
print(b)