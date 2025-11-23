# Напишите программу, в которой создается текстовый файл. Имя файла вводится пользователем. 
# Текст для файла вводится пользователем. При записи текста в файл все маленькие буквы заменяются на большие.

#name = input('Enter name of file = ')
#txt = input('input text =')

name = 'name'
txt = 'test'

with open(f'E:\\github\\Py\\{name}.txt', 'w') as file:
    file.write(txt.upper())
