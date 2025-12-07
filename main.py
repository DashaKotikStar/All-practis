class UserDirectory:
    def __init__(self):
        self.ids = []      # список int
        self.phones = []   # список str

    def add_user(self, user_id: int, phone: str):
        self.ids.append(user_id)
        self.phones.append(phone)

    def sort_by_id(self):
        combined = list(zip(self.ids, self.phones))
        combined.sort(key=lambda x: x[0])
        self.ids, self.phones = zip(*combined) if combined else ([], [])
        self.ids = list(self.ids)
        self.phones = list(self.phones)

    def sort_by_phone(self):
        combined = list(zip(self.phones, self.ids))
        combined.sort(key=lambda x: x[0])
        self.phones, self.ids = zip(*combined) if combined else ([], [])
        self.phones = list(self.phones)
        self.ids = list(self.ids)

    def display(self):
        if not self.ids:
            print("Список пуст.")
            return
        print("\n--- Список пользователей ---")
        for i in range(len(self.ids)):
            print(f"Код: {self.ids[i]:<5} | Телефон: {self.phones[i]}")

    def run_menu(self):
        print("=== Программа «справочник» ===")
        while True:
            print("\nМеню:")
            print("1. Отсортировать по идентификационным кодам")
            print("2. Отсортировать по номерам телефона")
            print("3. Вывести список пользователей с кодами и телефонами")
            print("4. Выход")

            choice = input("Выберите действие (1-4): ").strip()

            if choice == '1':
                self.sort_by_id()
                print("Список отсортирован по идентификационным кодам.")
            elif choice == '2':
                self.sort_by_phone()
                print("Список отсортирован по номерам телефона.")
            elif choice == '3':
                self.display()
            elif choice == '4':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")


class BookDirectory:
    def __init__(self):
        self.titles = []   # список строк — названия книг
        self.years = []    # список целых чисел — годы выпуска

    def add_book(self, title: str, year: int):
        self.titles.append(title)
        self.years.append(year)

    def sort_by_title(self):
        combined = list(zip(self.titles, self.years))
        combined.sort(key=lambda x: x[0])
        self.titles, self.years = zip(*combined) if combined else ([], [])
        self.titles = list(self.titles)
        self.years = list(self.years)

    def sort_by_year(self):
        combined = list(zip(self.years, self.titles))
        combined.sort(key=lambda x: x[0])
        self.years, self.titles = zip(*combined) if combined else ([], [])
        self.years = list(self.years)
        self.titles = list(self.titles)

    def display(self):
        if not self.titles:
            print("Список книг пуст.")
            return
        print("\n--- Список книг ---")
        for i in range(len(self.titles)):
            print(f"Название: {self.titles[i]:<30} | Год: {self.years[i]}")

    def run_menu(self):
        print("=== Программа «книги» ===")
        while True:
            print("\nМеню:")
            print("1. Отсортировать по названию книги")
            print("2. Отсортировать по годам выпуска")
            print("3. Вывести список книг с названиями и годами выпуска")
            print("4. Выход")

            choice = input("Выберите действие (1-4): ").strip()

            if choice == '1':
                self.sort_by_title()
                print("Список отсортирован по названию книг.")
            elif choice == '2':
                self.sort_by_year()
                print("Список отсортирован по годам выпуска.")
            elif choice == '3':
                self.display()
            elif choice == '4':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")



def main():
    print("=== Выберите программу ===")
    print("1. Программа «справочник» (ID и телефон)")
    print("2. Программа «книги» (название и год)")
    choice = input("Введите 1 или 2: ").strip()

    if choice == '1':
        print("\n--- Программа «справочник» ---")
        try:
            count = int(input("Сколько записей вы хотите добавить? "))
        except ValueError:
            print("Неверный ввод. Установлено 0 записей.")
            count = 0

        directory = UserDirectory()
        for i in range(count):
            try:
                user_id = int(input(f"Введите ID для записи {i+1}: "))
                phone = input(f"Введите телефон для записи {i+1}: ")
                directory.add_user(user_id, phone)
            except ValueError:
                print("Неверный формат ID. Пропущено.")
                continue

        directory.run_menu()

    elif choice == '2':
        print("\n--- Программа «книги» ---")
        try:
            count = int(input("Сколько книг вы хотите добавить? "))
        except ValueError:
            print("Неверный ввод. Установлено 0 книг.")
            count = 0

        library = BookDirectory()
        for i in range(count):
            title = input(f"Введите название книги {i+1}: ")
            try:
                year = int(input(f"Введите год выпуска книги {i+1}: "))
            except ValueError:
                print("Неверный формат года. Установлено 0.")
                year = 0
            library.add_book(title, year)

        library.run_menu()

    else:
        print("Неверный выбор. Программа завершена.")


if __name__ == "__main__":
    main()