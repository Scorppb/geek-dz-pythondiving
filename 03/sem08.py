# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.


friends_items = {
    "Иван": ("палатка", "спальник", "фонарик"),
    "Петр": ("спальник", "котелок", "еда"),
    "Семен": ("спальник", "фонарик", "топор")
}

all_friends = list(friends_items.keys())
all_items = set.intersection(*[set(items) for items in friends_items.values()])

unique_items = set()
for items in friends_items.values():
    unique_items.update(set(items))

shared_items = {}
for friend, items in friends_items.items():
    other_friends = all_friends.copy()
    other_friends.remove(friend)
    other_items = set.union(*[set(friends_items[other_friend]) for other_friend in other_friends])
    diff_items = set(items) - other_items
    if diff_items:
        shared_items[friend] = diff_items

print(f'Вещи, которые взяли все друзья: {all_items}')
print(f'Уникальные вещи, есть только у одного друга: {unique_items - all_items}')
print(f'Вещи, которые есть у всех кроме одного друга и имя друга: {shared_items}')

