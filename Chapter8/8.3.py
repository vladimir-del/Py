# Напишите программу, в которой описан класс. У объектов класса должно быть поле, представляющее собой числовой список. 
# Этот список формируется на основе списка, переданного конструктору в качестве аргумента. При этом из списка-аргумента 
# в список-поле включаются только числовые элементы (элементы других типов игнорируются). Необходимо также описать метод, 
# отображающий содержимое поля-списка, а также метод, вычисляющий среднее значение элементов поля-списка 
# (сумма значений элементов, деленная на их количество).




class my:
    """
    Description for this class
    """
    def __init__(self, a):
        self.my_list = []
        for l in a:
            if type(l) == int:
                self.my_list.append(l)
    def show(self):
        for l in range(len(self.my_list)): print(f'my_list [{l}]= {self.my_list[l]}')


    def avg(self):
        self.avg_list = sum(self.my_list) / len(self.my_list)
        print(f'Average list= {self.avg_list}')

    def dict_(self):
        print(self.__dict__)

    def class_(self):
        for key, value in self.__class__.__dict__.items():
            print(f'{key} : {value}')

arg = [4,4,4,'h',4]
A = my(arg)


A.show()
A.avg()
A.dict_()
A.class_()

