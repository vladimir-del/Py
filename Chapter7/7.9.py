# Напишите программу, в которой пользователь вводит имя текстового файла, 
# а программа отображает содержимое этого файла, а также создает копию 
# этого файла с пронумерованными строками.

#name = input('Введите имя файла= ')

name = 'my'


A = open(f'E:\\github\\Py\\{name}.txt', 'r')
B = open(f'E:\\github\\Py\\{name}_1.txt', 'w+')

L = A.readline()
k=1
while L != '':
    L = '['+str(k)+']' + L
    B.write(L)
    k += 1
    L = A.readline()
A.close()
B.close()


