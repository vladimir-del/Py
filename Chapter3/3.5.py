# напишите программу в которой создаеться вложенный список 
# из случайных чисел. В матрице которая создается данным 
# вложенным списком, удаляется строка и столбец. Номер 
# строки и столбца задается пользователем.

from random import *

def show(a):
    for i in a:
        for j in i:
            print(j, ' ', end='')
        print()



def matrix(a,b):
    res = [[randint(0,9) for i in range(a)] for j in range(b)]
    return res

a = matrix(6,3)

show(a)

DelRow = int(input('Введите номер строки для удаления='))
DelCol = int(input('Введите номер столбца для удаления='))

new_matrix = [row[:DelCol] + row[DelCol + 1:] for row in (a[:DelRow] + a[DelRow + 1:])]

show(new_matrix)