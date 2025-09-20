# Напишите программу, в которой создается два списка 
# одинакового размера. На основе этих списков поочередной 
# вставкой элементов из первого и второго списка 
# формируется новый список.

from random import * 

a = [randint(0,3) for i in range(3)]

b = [randint(0,3) for i in range(3)]
c=[]
for i in range(len(a)):
    c.append(a[i])
    c.append(b[i])

print(a)
print(b)
print(c)