# 1.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше
# суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить
# является ли треугольник разносторонним, равнобедренным или равносторонним.

def input_numbers(inputText):
    check_input = False
    while not check_input:
        try:
            number = float(input(f'{inputText}'))
            check_input = True
        except ValueError:
            print('Вы вводите не цифры, введите корректные данные')
    return number

def check_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        if a == b == c:
            return 'Триугольник равносторонний'
        elif a == b or b == c or a == c:
            return 'Триугольник равнобедренный'
        else:
            return 'Треугольник разносторонний'
    else:
        return 'Треугольник не существует.'


a = input_numbers('Введите сторону треугольника а: ')
b = input_numbers('Введите сторону треугольника b: ')
c = input_numbers('Введите сторону треугольника c: ')

result = check_triangle(a, b, c)
print(result)