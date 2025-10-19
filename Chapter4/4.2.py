# Напишите программу, в которой пользователь вводит два 
# целых числа, а программой определяются цифры, которые 
# есть в представлении обоих чисел.

a = int(input('Введите первое целое число='))
b = int(input('Введите второе целое число='))
union1 = set()
union2 = set()
while a:
    temp = a%10
    union1.add(temp)
    a //= 10

while b:
    temp = b%10
    union2.add(temp)
    b //= 10


c = set()
c = union1 & union2
print(c)