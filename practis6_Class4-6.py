# Задание 4:
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        # Проверка, что все стороны - числа
        if not all(isinstance(side, (int, float)) for side in [self.a, self.b, self.c]):
            return "Нужно вводить только числа!"

        # Проверка, что все стороны положительные
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"

        # Проверка, можно ли построить треугольник
        if ( (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)):
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."


def task_4():
    print("--- Задание 4: Проверка треугольника ---")
    print("Введите длины трёх отрезков:")
    try:
        a = float(input("Первый отрезок: "))
        b = float(input("Второй отрезок: "))
        c = float(input("Третий отрезок: "))
    except ValueError:
        print("Нужно вводить только числа!")
        return

    checker = TriangleChecker(a, b, c)
    result = checker.is_triangle()
    print(result)


# Задание 5:
class Nikola:
    def __init__(self, name, age):
        if name != "Николай":
            self.name = f"Я не {name}, а Николай"
        else:
            self.name = name
        self.age = age

    def __setattr__(self, key, value):
        # key — имя атрибута (например, "patronymic")
        # value — значение (например, "Иванович")
        # Запрещаем добавлять новые атрибуты, кроме name и age
        if key not in ["name", "age"]:
            raise AttributeError(f"Нельзя добавить атрибут '{key}'")
        super().__setattr__(key, value)


def task_5():
    print("\n--- Задание 5: Класс Nikola ---")
    name = input("Введите имя: ").strip()
    try:
        age = int(input("Введите возраст: "))
    except ValueError:
        print("Возраст должен быть числом.")
        return

    person = Nikola(name, age)
    print(f"Имя: {person.name}")
    print(f"Возраст: {person.age}")

    # Попробуем добавить новый атрибут — будет ошибка
    try:
        new_attr = input("Хотите попробовать добавить 'отчество'? Введите 'да', если хотите: ").strip()
        if new_attr.lower() == "да":
            person.patronymic = "Иванович"
    except AttributeError as e:
        print(f"Ошибка: {e}")


# Задание 6:
class Programmer:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.worked_hours = 0
        self.salary = 0

        # Оклады
        self.hourly_rates = {
            "Junior": 10,
            "Middle": 15,
            "Senior": 20
        }
        self.rate = self.hourly_rates.get(self.position, 0)
        self.senior_bonus = 0  # повышения для Senior

    def work(self, time):
        self.worked_hours += time
        if self.position == "Senior":
            rate = self.rate + self.senior_bonus
        else:
            rate = self.rate
        self.salary += time * rate
    def rise(self):
        if self.position == "Junior":
            self.position = "Middle"
            self.rate = self.hourly_rates["Middle"]
        elif self.position == "Middle":
            self.position = "Senior"
            self.rate = self.hourly_rates["Senior"]
        elif self.position == "Senior":
            self.senior_bonus += 1  # повышение +1 тугрик

    def info(self):
        return f"{self.name} {self.worked_hours}ч. {self.salary} тгр"


def task_6():
    print("\n--- Задание 6: Класс Programmer ---")
    name = input("Введите имя программиста: ").strip()
    position = input("Введите должность (Junior, Middle, Senior): ").strip()

    if position not in ["Junior", "Middle", "Senior"]:
        print("Неверная должность. Должна быть одна из: Junior, Middle, Senior.")
        return

    prog = Programmer(name, position)

    while True:
        print("\nВыберите действие:")
        print("1 — Работать (указать количество часов)")
        print("2 — Повыситься")
        print("3 — Информация о сотруднике")
        print("4 — Выход")
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            try:
                hours = int(input("Сколько часов отработали? "))
                prog.work(hours)
                print(f"Отработано {hours} часов.")
            except ValueError:
                print("Количество часов должно быть числом.")
        elif choice == "2":
            prog.rise()
            print("Повышение выполнено.")
        elif choice == "3":
            print(prog.info())
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


# === Основной код ===
if __name__ == "__main__":
    task_4()
    task_5()
    task_6()