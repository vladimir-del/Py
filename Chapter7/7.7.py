# Напишите программу, в которой пользователь вводит две даты, а программа определяет количество полных дней между этими датами.


from datetime import * 


#date_A = input('Введите дату #1 в формате dd/mm/yyyy= ')
#date_B = input('Введите дату #2 в формате dd.mm.yyyy= ')
date_A = "23/11/25"
date_B = "13/11/25"

a = datetime.strptime(date_A, "%d/%m/%y")
b = datetime.strptime(date_B, "%d/%m/%y")
c = a - b

print(f'Между введенными датами {c.days} дней')