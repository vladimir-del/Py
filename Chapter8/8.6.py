# Напишите программу, в которой описан класс и функция, предназначенная для создания списка из объектов. 
# У объектов класса должно быть поле (предназначенное для записи целочисленных значений). При вызове 
# функции аргументом ей передается целое число, определяющее количество объектов в списке. Поля объектов 
# заполняются целыми нечетными числами


import random as rd

class my:
    def __init__(self):
        self.value = rd.choice([x for x in range(1,10) if x % 2 != 0])

    def show(self):
        print(f'У класса {self.__class__.__name__} переменная Value= {self.value} ')

def f(n) -> list:
    my_list =[]
    for l in range(n):
        my_list.append(my())
    return my_list


def show(lst):
    for i in lst:
        for k, v in i.__dict__.items():
            print(f'Значение поля объекта {i}  {k} = {v}')
 
rez = f(5)

for i in rez:
    my.show(i)
    
show(rez)



