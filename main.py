def is_iterable(obj):
    try:
        iter(obj)
        return True
    except:
        False


def personal_sum(numbers):
    result = int()
    incorrect = 0
    for x in numbers:
        try:
            result += x
        except TypeError as exc:
            print(f'Некорректный тип данных для подсчёта суммы - {x}')
            incorrect += 1
    return (result, incorrect)


def calculate_average(numbers):
    if is_iterable(numbers):
        tup = personal_sum(numbers)
        if tup[1] == len(numbers):
            return 0
        else:
            try:
                res = tup[0]/(len(numbers) - tup[1])
                return res
            except ZeroDivisionError:
                print('Деление на ноль!')



    else:
        print('В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

a = 10
