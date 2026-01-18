import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_correlations_simple(df: pd.DataFrame) -> None:
    """
    Строит графики зависимости оценки от разных факторов.
    Показывает корреляции и дает базовые рекомендации.
    """
    
    # Факторы для анализа
    factors = ["hours_studied", "attendance", "sleep_hours", 
               "motivation", "tutoring_sessions", "family_income"]
    
    print("=== АНАЛИЗ КОРРЕЛЯЦИЙ ===")
    
    # Для хранения коэффициентов корреляции
    correlations = {}
    
    # Создаем графики
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    axes = axes.flatten()
    
    for i, factor in enumerate(factors):
        ax = axes[i]
        
        # scatter plot
        ax.scatter(df[factor], df['exam_score'], alpha=0.5, s=30)
        
        # Линия тренда
        z = np.polyfit(df[factor], df['exam_score'], 1)
        p = np.poly1d(z)
        ax.plot(df[factor], p(df[factor]), "r--", alpha=0.8)
        
        # Вычисляем корреляцию
        corr = df[factor].corr(df['exam_score'])
        correlations[factor] = corr
        
        # Заголовок с корреляцией
        ax.set_title(f"{factor}\nкорр = {corr:.2f}", fontsize=11)
        ax.set_xlabel(factor)
        ax.set_ylabel('Оценка')
        
        # Сетка для наглядности
        ax.grid(True, alpha=0.3)
        
        # Выводим в консоль
        print(f"{factor}: корреляция = {corr:.3f}")
    
    plt.suptitle("Влияние факторов на оценку за экзамен", fontsize=14)
    plt.tight_layout()
    plt.show()
    
    # Рекомендации
    print("\n=== РЕКОМЕНДАЦИИ ===")
    
    # Находим топ-20% студентов
    top_threshold = df['exam_score'].quantile(0.8)
    top_students = df[df['exam_score'] >= top_threshold]
    
    if len(top_students) > 0:
        print(f"У топ-20% студентов (оценка > {top_threshold:.1f}):")
        
        for factor in factors[:3]:  
            avg_top = top_students[factor].mean()
            avg_all = df[factor].mean()
            
            if factor == "hours_studied":
                print(f"• Учатся в среднем {avg_top:.1f} часов (все: {avg_all:.1f} часов)")
            elif factor == "attendance":
                print(f"• Посещаемость {avg_top:.1f}% (все: {avg_all:.1f}%)")
            elif factor == "sleep_hours":
                print(f"• Спит {avg_top:.1f} часов (все: {avg_all:.1f} часов)")
    
    # Самый важный фактор
    most_important = max(correlations, key=correlations.get)
    print(f"\nСамый важный фактор: {most_important} (корр = {correlations[most_important]:.3f})")
    
    return correlations


def simple_recommendations(df: pd.DataFrame):
    """
    Рекомендации на основе данных.
    """
    print("\n=== СОВЕТЫ ДЛЯ СТУДЕНТОВ ===")
    
    # Топ-20%
    top_threshold = df['exam_score'].quantile(0.8)
    top_students = df[df['exam_score'] >= top_threshold]
    
    if len(top_students) == 0:
        print("Недостаточно данных для анализа.")
        return
    
    # Средние значения для топ-студентов
    avg_hours = top_students['hours_studied'].mean()
    avg_attendance = top_students['attendance'].mean()
    avg_sleep = top_students['sleep_hours'].mean()
    
    print("Чтобы попасть в топ-20% студентов:")
    print(f"1. Учитесь примерно {avg_hours:.0f} часов в неделю")
    print(f"2. Посещайте минимум {avg_attendance:.0f}% занятий")
    print(f"3. Спите около {avg_sleep:.0f} часов в сутки")
    
    # Анализ мотивации
    if 'motivation' in df.columns:
        avg_motivation = top_students['motivation'].mean()
        print(f"4. Поддерживайте мотивацию на уровне {avg_motivation:.1f}/10")
