# Напишите программу с классом, объекты которого можно индексировать. В частности, 
# у объекта должно быть два поля-списка с числами. При индексировании объекта 
# возвращается сумма элементов из списков с соответствующим индексом. Если 
# в каком-то списке нет такого элемента, он заменяется нулевым значением.

class a:

    def __init__(self, lst1, lst2):
        self.lst1 = lst1
        self.lst2 = lst2

    def __getitem__(self, index):
        val1 = self.lst1[index] if index < len(self.lst1) else 0
        val2 = self.lst2[index] if index < len(self.lst2) else 0
        return val1 + val2

    def __str__(self):
        return str(self.lst1) + str(self.lst2)
o = a([1,2,3], [4,5,6])

print(o[5])
print(o[2])
