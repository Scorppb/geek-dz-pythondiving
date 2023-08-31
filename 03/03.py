# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи
# влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

def input_numbers(input_text):
    check_input = False
    while not check_input:
        try:
            number = float(input(f'{input_text}'))
            check_input = True
        except ValueError:
            print('Вы вводите не цифры, введите корректные данные')
    return number

def cargo_collection(items, max_weight):
    cargo = []
    for item, weight in items.items():
        if weight <= max_weight:
            cargo.append(item)
            max_weight -= weight
    return cargo


backpack_volume = input_numbers('Введите объём Вашего рюкзака: ')
items = {
    "Нож": 0.1,
    "Компас": 0.3,
    "Спички": 0.1,
    "Фонарик": 0.5,
    "Аптечка": 0.5,
    "Тент": 3.0,
    "Рация": 0.5,
    "Карта": 0.1,
    "Тушенка": 0.5,
    "Кружка, ложка, миска": 1.0,
    "Спальник": 2,
    "Топор": 1.0,
    "Ружье, патроны": 5.0,
    "Веревка": 1.0,
    "Смартфон": 0.5,
    "Пшенка": 1.0,
    "Перловка": 1.0,
    "Гречка": 1.0,
    "Рис": 1.0
}

print(f"Примерный список вещей составляет: \n{cargo_collection(items, backpack_volume)}")




