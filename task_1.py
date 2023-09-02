
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def na_hex(num):
    hex_digits = '0123456789abcdef'
    hex_str = ''
    while num > 0:
        hex_str = hex_digits[num % 16] + hex_str
        num = num // 16
    return hex_str


butin_san = int(input('Введите целое число: '))
hex_str = na_hex(butin_san)
print(f'Шестнадцатеричное представление числа {butin_san} ---> 0x{hex_str}')
print('----------------')
print(f'Проверка на hex функцей hex(): {hex(butin_san)}')

if hex(butin_san) == ('0x'+hex_str):
    print('Программа работает правильно! Ураааа!')
else:
    print('Программа не правильно работает!((((')
