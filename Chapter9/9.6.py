# Напишите программу, в которой для объектов класса предусмотрен 
# специальный режим доступа к полям. В частности, у объекта должно 
# быть поле-список, значением которому можно присваивать только список.
# Из присваиваемого списка в поле-список копируются только  текстовые значения. 
# При считывании значения этого поля возвращается текстовая строка, 
# содержащая только начальные буквы текстовых значений, которые входят в список.

class a:

    def __init__(self):
        self.lst = []

    def __setattr__(self, name, value):
        if type(value) == list:
            self.__dict__[name] = list(filter(lambda x: type(x) is str, value))
        else:
            raise TypeError('not list')
        
    def __getattribute__(self, name):
        if name == 'lst':
            return [letter[0] for letter in ' '.join(self.__dict__[name]).split()]
        else:
            return object.__getattribute__(self, name)

    def __repr__(self):
        return f'ob.lst = {self.lst}'


ob1 = a()

ob1.lst = [1, 'tetet', 5, 'ff']

print (ob1)