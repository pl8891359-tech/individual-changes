import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_correlations(df: pd.DataFrame) -> None:
    """
    Строит scatter-графики зависимости экзаменационного балла
    от каждого выбранного фактора.
    """

    # сортировка по оценке
    df = df.sort_values("exam_score")

    # список факторов, которые сравниваем с экзаменом
    factors = [
        "hours_studied",
        "attendance",
        "sleep_hours",
        "motivation",
        "tutoring_sessions",
        "family_income"
    ]

    # строим отдельный график для каждого фактора
    for col in factors:
        plt.figure(figsize=(6, 4))
        sns.scatterplot(data=df, x=col, y="exam_score")
        plt.title(f"Exam Score vs {col}")
        plt.xlabel(col)
        plt.ylabel("exam_score")
        plt.tight_layout()
        plt.show()