# функция нахождения паттернов в которую мы передаем наши данные и столбец в котором ищем паттерн
def find_pattern(df, column_name):
    # находим максимальное значение в столбце и создаем массив такого размера
    max_val = int(df[column_name].max())
    arr1 = [0] * max_val

    # находим погрешность в нашем случае берем 10%
    inaccuracy = int(max_val / 10)

    # проходимся по всем возможным значениям для столбца и записываем для каждого сколько значений в его окрестности
    for i in range(1, max_val + 1):
        for index, row in df.iterrows():
            val = row[column_name]
            if i - inaccuracy <= val <= i + inaccuracy: arr1[i - 1] += 1

    # если есть значения с мощностью 5 и больше, то будем считать их паттерном
    if max(arr1) > 4:
        # проверяем одно ли у нас значение с наибольшей мощностью если нет то пишем рендж в котором у нас находиться
        last_max_index = len(arr1) - 1 - arr1[::-1].index(max(arr1))
        if arr1.index(max(arr1)) == last_max_index:
            print(f"pattern of {column_name}:{arr1.index(max(arr1))} ")
        else:
            print(f"pattern of {column_name} :{arr1.index(max(arr1))} - {last_max_index} ")


# функция, которая получает список из 10 учеников лучших или худших
def patterns_top10(df):
    # создаем список всех столбцов в которых нужно найти паттерн
    columns_to_analyze = [col for col in df.columns if col != 'exam_score']

    # для каждого столбца начинаем поиск паттерна
    for column_name in columns_to_analyze:
        find_pattern(df, column_name)
    return None


def patterns(df):
    # проверяем, удалось ли загрузить данные
    if df is None or df.empty:
        print("Ошибка: передан пустой DataFrame")
        return None
    # Сортируем таблицу студентов по столбцу "exam_score"
    sorted_df = df.sort_values(by="exam_score", ascending=False)

    # запускаем поиск паттернов для 10 лучших студентов
    print("паттерны для лучших 10 учеников")
    patterns_top10(sorted_df.head(10))

    # запускаем поиск паттернов для 10 худших студентов
    print("паттерны для худших 10 учеников")
    patterns_top10(sorted_df.tail(10))