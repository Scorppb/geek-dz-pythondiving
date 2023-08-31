# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.


from fractions import Fraction

def gcd(a, b): 
    if a > b:   
        temp = b 
    else: 
        temp = a 
    for i in range(1, temp + 1): 
        if(( a % i == 0) and(b % i == 0 )): 
            gcd = i 
    return gcd 


def summation(string1, string2):
    a1, b1 = str(string1).split(sep="/")
    a2, b2 = str(string2).split(sep="/")
    a = int(a1)*int(b2) + int(a2)* int(b1)
    b = int(b1) * int(b2)
    divider = gcd(a, b)
    if divider == 1 and b !=1:
        return f"{a}/{b}"
    elif a == b:
        return "1"
    elif b == 1:
        return a
    else:
        return f"{a/divider:.0f}/{b/divider:.0f}"


def multiplication(string, string2):
    a1, b1 = str(string1).split(sep="/")
    a2, b2 = str(string2).split(sep="/")
    a = int(a1)*int(a2)
    b = int(b1) * int(b2)
    divider = gcd(a, b)
    if divider == 1 and b !=1:
        return f"{a}/{b}"
    elif a == b:
        return "1"
    elif b == 1:
        return a
    else:
        return f"{a/divider:.0f}/{b/divider:.0f}"

string1 = input("Введите дробь вида а/b: ")
string2 = input("Введите дробь вида c/d: ")

print(f"Сумма дробей {string1} и {string2} равна {summation(string1, string2)}")
print(f"Проверка {Fraction(string1) + Fraction(string2)}")
print(f"Произведение дробей {string1} и {string2} равно {multiplication(string1, string2)}")
print(f"Проверка {Fraction(string1) * Fraction(string2)}")