# Напишите программу, в которой описана функция, предназначенная для создания объектов.
# Функции при вызове передается список и текстовый аргумент. Текстовый аргумент определяет название класса, на основе
# которого создается объект. Текстовые элементы из списка определяют названия полей объекта (нетекстовые аргументы игнорируются).
# Значениями полей объекта являются натуральные числа


import random as rn



def F(lst, name) -> object | None:
    class my:


        def __init__(self):
            k = 0
            for s in lst:
                if type(s) == str:
                    self.__dict__[s] = rn.randint(1,9)
                    k +=1
                else:
                    continue

        def show(self):
           for k, v in self.__dict__.items():
               print(f'arg = {k}, value= {v}')       
            
    my.__name__ = name
    return my()

name_arg = 'obj'
list_arg = ['arg1', 'arg2', 'arg3', 35]

A = F(list_arg, name_arg)

A.show()



