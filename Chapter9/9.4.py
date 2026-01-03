# Напишите программу, в которой для объектов предусмотрены операции сложения с числом, 
# вычитания числа и вычитания из числа, а также  умножения на число и деления на число. 
# У объекта должно быть поле с числовым значением, и при выполнении указанных операций 
# они должны выполняться с полем объекта.


class a:


    def __init__(self, num):
        self.code = num

    def __add__(self, n):
        if type(n) == int:
            val = self.code + n
            return a(val)
        else:
            val = 0
            return a(val)
        
    def __sub__(self, n):
        if type(n) == int:
            val = self.code - n
            return a(val)
        else:
            val = 0
            return a(val)
        
    def __rsub__(self, n):
        if type(self.code) == int:
            val = n - self.code
            return a(val)
        else:
            val = 0
            return a(val)

    # def __str__(self):
    #     return str(self.code)

    def __repr__(self):
         return f'result ={self.code}'

obj_a = a(5)
obj_c = 24 - obj_a
print(obj_c)