# Напишите программу, в которой создается цепочка наследования 
# из трех классов. У объекта исходного класса имеется поле, и у 
# каждого следующего класса добавляется по одному полю. Опишите 
# методы, переопределяемые в производных классах, которые позволяют 
# присваивать значения полям и отображать значения полей.

class A:
    def __init__(self,num_A):
        self.value_A = num_A
    
    def set(self, new_num_A):
        self.value_A = new_num_A

    def show(self):
        print(f'Value_A = {self.value_A}')
        
class B(A):
    def __init__(self,num_A, num_B):
        A.__init__(self, num_A)
        self.value_B = num_B
    
    def set(self, new_num_A, new_num_B):
        A.set(self, new_num_A)
        self.value_B = new_num_B

    def show(self):
        A.show(self)
        print(f'Value_B = {self.value_B}')

class C(B):
    def __init__(self,num_A, num_B, num_C):
        B.__init__(self,num_A, num_B)
        self.value_C = num_C

    def set(self,num_A, num_B, num_C):
        B.set(self,num_A, num_B)
        self.value_C = num_C

    def show(self):
        super().show()
        print(f'Value_C = {self.value_C}')


cl1 = A(1)
cl1.show()
cl1.set(2)
cl1.show()

cl2 = B(3,4)
cl2.show()
cl2.set(5,6)
cl2.show()

cl3 = C(7,8,9)
cl3.show()
cl3.set(10,11,12)
cl3.show()