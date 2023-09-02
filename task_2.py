
# Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.


from fractions import Fraction
import math


a = '8/4'
b = '9/3'

def sokrFraction(a: int, b: int):             # бүтін санды қысқарту
    if a > b:
        c = a
    else:
        c = b
    while c != 1:
        if a % c == 0 and b % c == 0:
            return str(a // c) + '/' + str(b // c)
        else:
            c -= 1
    return str(a) + '/' + str(b)

def sum_fractions(a, b):                        # екі бөлшекті қосу әдісі
    num1 = a.split('/')
    num2 = b.split('/')
    lcm_fraction = math.lcm(int(num1[1]), int(num2[1]))   # НОЗ дроби
    numeratorFraction1 = int(lcm_fraction / int(num1[1]) * int(num1[0]))
    numeratorFraction2 = int(lcm_fraction / int(num2[1]) * int(num2[0]))
    return sokrFraction(numeratorFraction1 + numeratorFraction2, lcm_fraction)

def umn_fraction(a,b):                          # екі бөлшекті көбейту әдісі
    num1 = a.split('/')
    num2 = b.split('/')
    return sokrFraction(int(num1[0]) * int(num2[0]), int(num1[1]) * int(num2[1]))

def prov_fraction(a, b, operation):              # Fraction функциясында бөлшектерді есептеуді тексеру әдісі
    num1 = a.split('/')
    num2 = b.split('/')
    if operation == '*':
        return Fraction(int(num1[0]), int(num1[1])) * Fraction(int(num2[0]), int(num2[1]))
    elif operation == '+':
        return Fraction(int(num1[0]), int(num1[1])) + Fraction(int(num2[0]), int(num2[1]))
    elif operation == '-':
        return Fraction(int(num1[0]), int(num1[1])) - Fraction(int(num2[0]), int(num2[1]))
    else:
        return Fraction(int(num1[0]), int(num1[1])) / Fraction(int(num2[0]), int(num2[1]))

print('Расчет по программе:')
print(f'{a} * {b} = {umn_fraction(a, b)}')

print(f'{a} + {b} = {sum_fractions(a, b)}')
print('----------')
print('Проверка по Fraction:')
print(f'{a} * {b} = {prov_fraction(a, b, "*")}')
print(f'{a} + {b} = {prov_fraction(a, b, "+")}')

