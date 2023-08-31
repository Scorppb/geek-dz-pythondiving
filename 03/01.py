# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.


def remove_duplicates(source_list):

    my_set = set()

    for item in source_list:
        if source_list.count(item) > 0:
            my_set.add(item)

    return list(my_set)


source_list = [1, 3, 3, 2, 5, 7, 2, 6, 9, 5, 6, 1, 2, 2, 4]
print(f"Исходный список {source_list}")
print(f"Список без дубликатов {remove_duplicates(source_list)}")

