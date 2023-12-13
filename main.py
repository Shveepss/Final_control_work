def filter_strings(arr):
    result = []
    for string in arr:
        if len(string) <= 3:
            result.append(string)
    return result


# Получаем строки от пользователя и размещаем в массив
input_array = input("Введите строки через запятую: ").split(",")

# Получаем новый массив согласно условию
result_array = filter_strings(input_array)

# Выводим массив на экран
print("Результат:", result_array)
