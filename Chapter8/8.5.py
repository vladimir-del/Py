# Напишите программу, в которой описывается функция, предназначенная для создания объекта. Объект создается на 
# основе уже существующего объекта, который передается функции в качестве аргумента. В создаваемый объект
# добавляются только те неслужебные поля из исходного объекта, которые имеют целочисленное значение

class first:
    def __init__(self):
        self.arg1 = 'arg1'
        self.arg2 = 34
        self.arg3 = "56"
        self.arg4 = 55
     

    def show(self):
        for k, v in self.__dict__.items():
            print(f'Atr = {k}')
            print(f'Value = {v}')
            print('----------')

def func(SourceClass):
    Out_class = SourceClass()
    for s, k in list(Out_class.__dict__.items()):
        if type(k) != int:
            del Out_class.__dict__[s]
    return Out_class

A = func(first)

A.show()