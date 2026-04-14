#ИНДИВИДУАЛЬНОЕ ЗАДАНИЕ 1
'''
import os

print("Проверка секретных ключей:")
print("API_KEY:", os.getenv("API_KEY"))
print("JWT_SECRET:", os.getenv("JWT_SECRET"))
print("LOG_TOKEN:", os.getenv("LOG_TOKEN"))
print("GRID_NODE_ID:", os.getenv("GRID_NODE_ID"))
print("ALERT_SECRET:", os.getenv("ALERT_SECRET"))
'''

#ИНДИВИДУАЛЬНОЕ ЗАДАНИЕ 2
import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt

# входные данные
requests_data = [5, 10, 20, 80, 150, 300, 250, 100, 40, 10]

status = []

# расчет
for r in requests_data:
    if r < 50:
        status.append("Норма")
    elif r < 100:
        status.append("Подозрительно")
    else:
        status.append("Атака")

# таблица
time = list(range(1, len(requests_data) + 1))
table = list(zip(time, requests_data, status))
df = pd.DataFrame(table, columns=["Время", "Запросы", "Статус"])

print("Анализ нагрузки:")
print(df)
print()

# линейный график нагрузки
plt.figure(figsize=(10, 6))
plt.plot(df["Время"], df["Запросы"], marker="o", label="Нагрузка")
plt.axhline(50, linestyle="--", label="Порог подозрительности")
plt.axhline(100, linestyle="--", label="Порог атаки")
plt.xlabel("Время")
plt.ylabel("Запросы")
plt.title("Линейный график нагрузки")
plt.legend()
plt.grid(True)
plt.savefig("line_chart.png", dpi=100, bbox_inches="tight")
plt.close()

# столбчатая диаграмма
plt.figure(figsize=(10, 6))
plt.bar(df["Время"], df["Запросы"])
plt.xlabel("Время")
plt.ylabel("Запросы")
plt.title("Столбчатая диаграмма нагрузки")
plt.grid(True)
plt.savefig("bar_chart.png", dpi=100, bbox_inches="tight")
plt.close()

# круговая диаграмма
counts = df["Статус"].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(counts.values, labels=counts.index, autopct="%1.1f%%")
plt.title("Распределение состояний нагрузки")
plt.savefig("pie_chart.png", dpi=100, bbox_inches="tight")
plt.close()

# сравнительный линейный график
normal = [r if r < 50 else 0 for r in requests_data]
suspicious = [r if 50 <= r < 100 else 0 for r in requests_data]
attack = [r if r >= 100 else 0 for r in requests_data]

plt.figure(figsize=(10, 6))
plt.plot(time, normal, marker="o", label="Норма")
plt.plot(time, suspicious, marker="s", label="Подозрительно")
plt.plot(time, attack, marker="^", label="Атака")
plt.xlabel("Время")
plt.ylabel("Запросы")
plt.title("Сравнение состояний нагрузки")
plt.legend()
plt.grid(True)
plt.savefig("compare_chart.png", dpi=100, bbox_inches="tight")
plt.close()

print("Графики успешно сохранены:")
print("line_chart.png")
print("bar_chart.png")
print("pie_chart.png")
print("compare_chart.png")

#ИНДИВИДУАЛЬНОЕ ЗАДАНИЕ 5
#поменяли строку
#requests = [5, 10, 20, 80, 150, 300, 250, 100, 40, 10]