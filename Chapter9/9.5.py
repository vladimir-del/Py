# Напишите программу, в которой для объектов класса предусмотрены 
# операции сравнения. У каждого объекта есть поле-список с числовыми 
# значениями. Операции сравнения выполняются так: объекты на предмет 
# равенства проверяются по первому элементу в списках, на предмет 
# «не равно» — по второму элементу в списках, «меньше» — по третьему 
# элементу в списках, и так далее. Если соответствующего элемента 
# в списке нет, используется нулевое значение.

LST1 = [1,2,2]
LST2 = [2,2,3]

arg1 = 3
arg2 = 3

class a:

    def __init__(self, lst):
        self.list = lst

    @classmethod
    def __verify(cls, other):
        if not isinstance(other, (list, a)):
           raise TypeError('not that type')
        return other if isinstance(other, int) else other.list[0]


    def __eq__(self, other):
        return self.list[0] == other.__verify(other)
    
    def __ne__(self, other):
        if not isinstance(other, (list, a)):
           raise TypeError('not that type')
        return self.list[1] != other.list[1]
    
    def __lt__(self, other):
        if not isinstance(other, (list, a)):
           raise TypeError('not that type')
        return self.list[2] < other.list[2]
    
    def __repr__(self):
        return f'lst = {self.list}'

ob1 = a(LST1)

ob2 = a(LST2)

print(ob1 == ob2)
print(ob1 != ob2)
print(ob1 < ob2)