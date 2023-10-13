import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних з CSV-файлу
data = pd.read_csv('lab2/police_project.csv')

# 1. Перевірка, білих чи темношкірих людей частіше зупиняє поліція.
race_counts = data['driver_race'].value_counts(normalize=True)
print("Частота зупинок за расою:")
print(race_counts)
race_counts.plot(kind="pie", figsize=(5, 5),fontsize=16)
plt.ylabel('Колір')
plt.title('Частота зупинок за расою')
plt.show()

# 2. Залежність частоти зупинок через наркотики від часу доби та побудова графіка
drug_stops_by_time = data[data['drugs_related_stop'] == True]['stop_time'].str.split(':').apply(lambda x: int(x[0])).value_counts().sort_index()
print("Частота зупинок через наркотики за годиною:")
print(drug_stops_by_time)
drug_stops_by_time.plot(color='red')
plt.xlabel('Година')
plt.ylabel('Кількість зупинок через наркотики')
plt.title('Частота зупинок через наркотики за годиною')
plt.show()

# 3. Графік типу hist для розподілу кількості зупинок за часом
data['stop_hour'] = data['stop_time'].str.split(':').apply(lambda x: int(x[0]))
data['stop_hour'].plot(kind='hist', bins=24, edgecolor='red', color='black')
plt.xlabel('Година')
plt.ylabel('Кількість зупинок')
plt.title('Розподіл кількості зупинок за годиною')
plt.show()

# 4. Заміна хибних даних в стовпці 'stop_duration' на NaN
data['stop_duration'] = pd.to_numeric(data['stop_duration'], errors='coerce')

# 5. Визначення середнього часу зупинки для кожної з причин зупинки та побудова графіку
mean_stop_duration = data.groupby('violation_raw')['stop_duration'].mean()
mean_stop_duration.plot(kind='bar')
plt.xlabel('Причина зупинки')
plt.ylabel('Середній час зупинки (хвилини)')
plt.title('Середній час зупинки для кожної причини зупинки')
plt.xticks(rotation=0)
plt.show()