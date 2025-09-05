# Функция возвращающая результатом второе по величине в списке
# переданном функции в качесте агрумента

up = int(input('input up limit='))

seq = list(k for k in range(1,up + 1))

def func1(arg):
    sorted(arg)
    print(arg[-2])

func1(seq)