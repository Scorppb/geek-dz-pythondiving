# 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу
# и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def input_numbers(input_text, MINIMAL, MAXIMAL):
    check_input = False
    while not check_input:
        try:
            a = int(input(f'{input_text}'))
            if MINIMAL <= a < MAXIMAL:
                check_input = True
            else:
                print(f'Число не попало в диапозон чисел от {MINIMAL} до {MAXIMAL}')
        except ValueError:
            print('Вы вводите не цифры, введите корректные данные')
    return a


def check_prime_number(x):
    for i in range(2, number):
        if not (number % i):
            print("Введенное число составное")
            exit()
    else:
        print('Введенное число простое')


MINIMAL = 0
MAXIMAL = 100000
number = input_numbers(f'Введите число от {MINIMAL} до {MAXIMAL}: ', MINIMAL, MAXIMAL)
check_prime_number(number)

