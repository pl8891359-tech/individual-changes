# Импортируем функцию load_and_prepare_data из файла parse.py
import pandas as pd

# Создаем функцию с параметром filename
def calculate_top20_averages(df: pd.DataFrame):

    # Сортируем таблицу студентов по столбцу "exam_score" 
    sorted_df = df.sort_values(by="exam_score", ascending=False)
    
    # Берем первые 20 строк из отсортированной таблицы
    top20 = sorted_df.head(20)
    
    # Считаем средний балл за экзамен для топ-20 студентов
    avg_exam_score = top20["exam_score"].mean()
    
    # Считаем среднее время учебы для топ-20 студентов
    avg_study_hours = top20["hours_studied"].mean()
    
    # Считаем среднее время сна для топ-20 студентов
    avg_sleep_hours = top20["sleep_hours"].mean()
    
    # Считаем среднюю посещаемость для топ-20 студентов
    avg_attendance = top20["attendance"].mean()
    
    # Считаем средний уровень мотивации для топ-20 студентов
    avg_motivation = top20["motivation"].mean()
    
    # Считаем среднее количество занятий с репетитором для топ-20 студентов
    avg_tutoring = top20["tutoring_sessions"].mean()
    
    # Считаем средний доход семьи для топ-20 студентов
    avg_income = top20["family_income"].mean()
    
    # Выводим заголовок результатов
    print("Средние показатели топ-20 студентов:")
    
    # Выводим средний балл за экзамен, округляя до 2 знаков после запятой
    print(f"Средний балл за экзамен: {avg_exam_score:.2f}")
    
    # Выводим среднее время учебы
    print(f"Среднее время учебы: {avg_study_hours:.2f} часов/неделю")
    
    # Выводим среднее время сна
    print(f"Среднее время сна: {avg_sleep_hours:.2f} часов/день")
    
    # Выводим среднюю посещаемость
    print(f"Средняя посещаемость: {avg_attendance:.2f}%")
    
    # Выводим средний уровень мотивации
    print(f"Средний уровень мотивации: {avg_motivation:.2f}")
    
    # Выводим среднее количество занятий с репетитором
    print(f"Средние занятия с репетитором: {avg_tutoring:.2f}")
    
    # Выводим средний доход семьи
    print(f"Средний доход семьи: {avg_income:.2f}")

if __name__ == "__main__":
    # Вызываем нашу основную функцию
    calculate_top20_averages()
