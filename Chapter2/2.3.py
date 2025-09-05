# программа которая на основе списка из натуральных чисел
# формирет целое число.

num = eval(input('input sequence number='))


i = len(num)
new = ''
while i>0:
    new = str(num[i-1]) + new
    i -= 1

new = int(new)
print(new, type(new))
