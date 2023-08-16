# 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1001

num = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Угадай число от 0 до 1000 за 10 попыток!")

for i in range(1, 11):
    my_num = int(input(f"У Вас попытка № {i}: "))
    if num > my_num:
        print(f"Число больше")
    elif num < my_num:
        print(f"Число меньше")
    else:
        print(f"Вы угадали число")
        exit()

print(f"Вы не угадали число")