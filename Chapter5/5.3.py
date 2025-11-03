# Напишите программу, в которой пользователю предлагается 
# ввести текст, а затем в этом тексте, без применения 
# специальных методов (а именно, не используя метод 
# swapcase()), все большие буквы меняются на маленькие, 
# а маленькие — на большие.

a = input('Введите текст= ')
num = 0

delta = ord('a') - ord('A')

a_new = ''
for k in a:
    if ord(k) > ord('A') and ord(k) < ord('Z'):
        a_new += chr(ord(k) + delta)
    elif ord(k) > ord('a') and ord(k) < ord('z'):
        a_new += chr(ord(k) - delta)
    else:
        a_new += k

print(f'Исходный текст = {a}')
print(f'Результат = {a_new}')
