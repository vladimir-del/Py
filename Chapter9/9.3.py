# Напишите программу, в которой для объектов класса определена 
# операция сложения. У каждого объекта есть поле-список, и при 
# сложении объектов получается новый объект того же класса. 
# Его поле-список получается объединением полей-списков исходных объектов.

class a:
    def __init__(self, inpt):
        self.my_list = inpt

    def __add__(self, othr):
        return a(self.my_list + othr.my_list)
    
    def __repr__(self):
         return (f"result= {self.my_list}")

obj_a = a([1,2])
obj_b = a([3,4])

obj_c = obj_a + obj_b

print(obj_c)


