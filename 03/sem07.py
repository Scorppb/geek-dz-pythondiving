# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.


my_string = input("Введите Ваш текст: ")

without_count_dict = {}
for i in my_string:
    without_count_dict[i] = without_count_dict[i]+1 if i in without_count_dict else 1

print(without_count_dict)

with_count_dict = {}
for i in set(my_string):
    with_count_dict[i] = my_string.count(i)

print(with_count_dict)
