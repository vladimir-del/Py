# Напишите программу, в которой есть класс с переопределенными 
# методами для приведения к разным типам. В частности, у объекта 
# должны быть поля с целочисленным значением, текстом и 
# действительным числовым значением. При приведении объекта к 
# целочисленному, текстовому или действительному числовому типу 
# возвращается значение соответствующего поля.

class my:
    def __init__(self, val):
        self.value = val

    def __int__(self):
        return self.value
        
    def __str__(self):
        return str('str = ') + str(self.value)
    
    def __float__(self):
        print('float =', end=' ')
        return self.value
        
a = my(4)

print(int(a))
a = my(str('s'))
print(a)

a = my(3.14)
print(float(a))
print(a)
    