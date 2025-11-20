# Напишите программу, в которой используется функция-генератор, 
# создающая итерируемый объект с названиями месяцев.

def f():
    L = [
        'january', 
        'february'
        ]
         
    for i in L:
        yield i

print(list(f()))
M = f()

for m in M:
    print(m)