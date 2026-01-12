# Напишите программу, в которой создается итератор, генерирующий
# числа Фибоначчи (первые два числа равны единице, а каждое следующее 
# есть сумма двух предыдущих). Количество генерируемых чисел передается
# в качестве аргумента конструктору при создании итератора.

class a:
    __a = 1
    __b = 1
    __generate = 0

    def __init__(self, qnt):
        self.qnt = qnt
        self.a = 1
        self.b = 1
        self.gen = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.gen < self.qnt:
            self.a, self.b = self.b, self.a + self.b
            self.gen +=1
            return self.b
        else:
            raise StopIteration

    def __repr__(self):
        return f'result=  {self.b}'

A = a(3)

print('1')
print('1')

for s in A:
    print(s)

B = a(5)
print('1')
print('1')
for s in range(5):
    print(next(B))

