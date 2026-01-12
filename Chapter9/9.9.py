# Напишите программу, в которой создается итератор, генерирующий 
# нечетные натуральные числа. Количество генерируемых чисел 
# определяется аргументом конструктора.

class a:
    """
    Docstring for a
    start - The start value of a sequence of natural numbers
    stop - The final value of the amount of the natural numbers
    """

    def __init__(self, start,  stop):
        self.stop = stop
        self.__CurrentValue = start
        self.__Generate = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__Generate < self.stop:
            if self.__CurrentValue % 2 != 0:
                res = self.__CurrentValue
                self.__CurrentValue += 2
                self.__Generate += 1
                return res
            else:
                self.__CurrentValue += 1
        else:
            raise StopIteration

    def __str__(self):
        return str(self.temp)

ob= a(2,5)

for s in ob:
    print(s)