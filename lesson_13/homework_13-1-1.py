import csv

# Шлях до файлів
file1_path = 'r-m-c.csv'
file2_path = 'rmc.csv'
output_path = 'rmc_clean.csv'

# Читання даних з файлів
def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)

data1 = read_csv(file1_path)
data2 = read_csv(file2_path)

# Злиття та видалення дублікатів
all_data = data1 + data2
unique_data = []
unique_set = set()

for row in all_data:
    row_tuple = tuple(row)  # Перетворюємо рядок на кортеж для додавання в множину
    if row_tuple not in unique_set:
        unique_set.add(row_tuple)
        unique_data.append(row)

# Запис результатів у новий файл
with open(output_path, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(unique_data)

print(f"Очищений файл записано як {output_path}")
