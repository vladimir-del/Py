# Напишите программу, в которой пользователь вводит момент времени, а программа определяет 
# интервал между текущим моментом и моментом времени, который указал пользователь.


from datetime import *

#date_A = input('Введите дату #1 в формате dd/mm/yyyy= ')
date_A = datetime.strptime('01/01/01', '%d/%m/%y')

def f(a):
    now = datetime.now()

    return now - a

print(f(date_A))