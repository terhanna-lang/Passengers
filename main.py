import json

# Функция ввода данных с оформлением в виде таблицы и сохранением в файл
def input_and_save(filename="passengers.json"):
    passengers = []
    
    # Вывод заголовка таблицы для ввода данных
    header = (
        "+----+------------------------------+-------------------------+-------------------------+-----------------+\n"
        "| №  |           ФИО                |  Пункт отправления      |  Пункт назначения       | Вес багажа (кг) |\n"
        "+----+------------------------------+-------------------------+-------------------------+-----------------+"
    )
    print(header)
    
    # Ввод данных для 15 пассажиров
    for i in range(15):
        print(f"\nВведите данные для пассажира #{i + 1}:")
        full_name = input("  ФИО: ")
        departure = input("  Пункт отправления: ")
        destination = input("  Пункт назначения: ")
        while True:
            try:
                weight = float(input("  Вес багажа (кг): "))
                break
            except ValueError:
                print("  Ошибка ввода! Введите числовое значение для веса багажа.")
        # Добавляем запись в список
        passengers.append({
            "full_name": full_name,
            "departure": departure,
            "destination": destination,
            "weight": weight
        })
    
    # Сохраняем данные в JSON-файл
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(passengers, f, ensure_ascii=False, indent=2)
    print("\nДанные успешно сохранены в файл.")

# Функция загрузки данных из файла
def load_passengers(filename="passengers.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

# Функция сортировки пассажиров по весу багажа (пузырьковая сортировка)
def sort_by_weight(passengers):
    n = len(passengers)
    for i in range(n):
        for j in range(n - i - 1):
            if passengers[j]["weight"] > passengers[j + 1]["weight"]:
                passengers[j], passengers[j + 1] = passengers[j + 1], passengers[j]
    return passengers

# Функция вывода списка пассажиров в виде таблицы
def print_passengers(passengers):
    print("\n+------------------------------+-------------------------+-----------------+")
    print("|           ФИО                |  Пункт отправления      | Вес багажа (кг) |")
    print("+------------------------------+-------------------------+-----------------+")
    for p in passengers:
        print(f"| {p['full_name']:<28} | {p['departure']:<23} | {p['weight']:>15.2f} |")
    print("+------------------------------+-------------------------+-----------------+")

# Основная программа
def main():
    # Если нужно ввести данные вручную, раскомментируйте следующую строку:
    # input_and_save()

    # Загрузка данных из файла (предварительно созданного, например, с помощью input_and_save)
    all_passengers = load_passengers()
    
    # Запрос пункта назначения для поиска
    dest = input("Введите пункт назначения для поиска: ")
    
    # Фильтрация пассажиров по введённому пункту назначения (без учета регистра)
    matched = [p for p in all_passengers if p["destination"].strip().lower() == dest.strip().lower()]
    
    if not matched:
        print("Нет пассажиров, следующих в указанный пункт.")
    else:
        # Сортируем найденные записи по возрастанию веса багажа
        sorted_passengers = sort_by_weight(matched)
        print(f"\nПассажиры, следующие в пункт назначения: {dest}")
        print_passengers(sorted_passengers)

if __name__ == "__main__":
    main()
