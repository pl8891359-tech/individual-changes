import pandas as pd
import os


# ЗАГРУЗКА И ОТБОР ДАННЫХ

def load_data(path: str) -> pd.DataFrame:
    """
    Загружает CSV-файл и отбирает необходимые столбцы
    """
    df = pd.read_csv(path)

    columns = {
        "Hours_Studied": "hours_studied",
        "Attendance": "attendance",
        "Sleep_Hours": "sleep_hours",
        "Exam_Score": "exam_score",
        "Motivation_Level": "motivation",
        "Tutoring_Sessions": "tutoring_sessions",
        "Family_Income": "family_income"
    }

    df = df[list(columns.keys())]
    df = df.rename(columns=columns)

    return df



# ПРОВЕРКА / ДОБАВЛЕНИЕ ID СТУДЕНТА

def ensure_student_id(df: pd.DataFrame) -> pd.DataFrame:
    """
    Проверяет наличие student_id и добавляет его при отсутствии
    """
    if "student_id" not in df.columns:
        df = df.reset_index(drop=True)
        df.insert(0, "student_id", df.index + 1)
    return df



# ПРОВЕРКА КАЧЕСТВА ДАННЫХ

def data_quality_report(df: pd.DataFrame) -> None:
    """
    Выводит краткую информацию о качестве данных
    """
    print("Размер датасета:", df.shape)
    print("Количество дубликатов:", df.duplicated().sum())
    print("Процент пропусков по столбцам:")
    print((df.isnull().mean() * 100).round(2))



# ОЧИСТКА И КОДИРОВАНИЕ

def clean_and_encode(df: pd.DataFrame) -> pd.DataFrame:
    """
    Обрабатывает пропуски и кодирует категориальные признаки
    """

    # Удаление дубликатов (кроме ID)
    df = df.drop_duplicates(subset=df.columns.drop("student_id"))

    numeric_cols = [
        "hours_studied",
        "attendance",
        "sleep_hours",
        "exam_score",
        "tutoring_sessions"
    ]

    # Заполнение пропусков медианой
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Кодирование категориальных признаков
    category_map = {
        "Low": 1,
        "Medium": 2,
        "High": 3
    }

    df["motivation"] = df["motivation"].map(category_map)
    df["family_income"] = df["family_income"].map(category_map)

    # Удаление строк с некорректными значениями
    df = df.dropna()

    return df



# ЭКСПОРТ ОЧИЩЕННЫХ ДАННЫХ

def export_clean_data(
    df: pd.DataFrame,
    path: str = "Data/cleaned_students.csv"
) -> None:
    """
    Сохраняет очищенный датасет в CSV
    """
    directory = os.path.dirname(path)

    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    df.to_csv(path, index=False)



# ГЛАВНЫЙ ПАЙПЛАЙН ПАРСИНГА

def parse_pipeline(path: str) -> pd.DataFrame:
    """
    Полный процесс подготовки данных
    """
    df = load_data(path)
    df = ensure_student_id(df)
    data_quality_report(df)
    df = clean_and_encode(df)
    export_clean_data(df)
    return df