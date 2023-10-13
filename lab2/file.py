import pandas as pd
import random
import string

# Створення умовних даних
data = {
    'driver_race': random.choices(['white', 'black'], k=1000),
    'drugs_related_stop': random.choices([True, False], k=1000),
    'stop_time': [f"{random.randint(0, 23)}:{random.randint(0, 59)}" for _ in range(1000)],
    'stop_duration': [random.randint(1, 59) for _ in range(1000)],
    'violation_raw': random.choices(['Speeding', 'DUI', 'Equipment', 'Other'], k=1000)
}
# Створення DataFrame
df = pd.DataFrame(data)
# Збереження даних у файл police_project.csv
df.to_csv('police_project.csv', index=False)