#целью этой программы является прогназирование оценки студента изходя из его посещаемости и количество потраченых
# на учебу часов, тк в резултате анализа таблицы была выявлена кореляция между этими показателями и итоговой оценкой
# Работу выполнил Немировский Матвей


#вычисляем среднее влияние фактора на оценку
def mid_impact(df, column_name):
    res = 0.0
    count = 0

    for i in range(len(df)):
        try:
            column_value = df[column_name].iloc[i]
            exam_score = df['exam_score'].iloc[i]

            if column_value != 0:
                res += float(exam_score) / column_value
                count += 1
        except:
            continue

    return res / count if count > 0 else 0.0


def predict(df):
    #считаем базовые влияния
    impact_hours_studied = mid_impact(df, 'hours_studied')
    impact_attendance = mid_impact(df, 'attendance')

    print(f"  Влияние hours_studied: {impact_hours_studied:.4f}")
    print(f"  Влияние attendance: {impact_attendance:.4f}")



    # создаем массив для хранения ошибок для разных коэффициентов [i, j, error]
    # Коэффициенты: i для hours (1-10), j для attendance (1-10) => 100 вариантов
    inaccuracies = [[0, 0, float('inf')] for _ in range(100)]


    idx = 0  # Индекс в массиве inaccuracies
    total_students = len(df)

    # Перебираем все комбинации коэффициентов
    for i in range(1, 11):  # Коэффициент для hours_studied (1-10)
        for j in range(1, 11):  # Коэффициент для attendance (1-10)

            # Сохраняем коэффициенты
            inaccuracies[idx][0] = i
            inaccuracies[idx][1] = j

            total_error = 0.0
            count = 0

            #для каждого студента вычисляем ошибку прогноза
            for student_idx in range(total_students):

                hours = df['hours_studied'].iloc[student_idx]
                attendance = df['attendance'].iloc[student_idx]
                actual_score = df['exam_score'].iloc[student_idx]

                #прогнозируем оценку
                pred = (hours * impact_hours_studied * i +
                        attendance * impact_attendance * j) / (i + j)

                #вычисляем ошибку по модулю
                error = abs(pred - actual_score)
                total_error += error
                count += 1

            # Сохраняем среднюю ошибку
            if count > 0:
                inaccuracies[idx][2] = total_error / count

            idx += 1

    #находим лучшую комбинацию коэффициентов проходя по массиву

    min_error = float('inf')
    min_index = -1

    for i in range(len(inaccuracies)):
        if inaccuracies[i][2] < min_error:
            min_error = inaccuracies[i][2]
            min_index = i

    # пишем результаты
    if min_index >= 0:
        best_i, best_j, best_error = inaccuracies[min_index]

        print(f"  Коэффициент для hours_studied: {best_i}")
        print(f"  Коэффициент для attendance: {best_j}")
        print(f"  Средняя ошибка: {best_error:.2f} баллов")

        print(f"\n4. ФОРМУЛА ПРОГНОЗА:")
        print( f"   Оценка = (часы × {impact_hours_studied:.2f} × {best_i} + посещаемость × {impact_attendance:.3f} × {best_j}) / ({best_i} + {best_j})")
