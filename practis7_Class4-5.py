import math

# Задание 4 — Класс Player
class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.exp_points = 0
        self.inventory = []

    def __str__(self):
        inv = ', '.join(self.inventory) if self.inventory else 'пусто'
        return f"Игрок: {self.nickname} | Опыт: {self.exp_points} | Инвентарь: {inv}"

    def addExp(self, exp):
        self.exp_points += exp

    def addItem(self, item):
        self.inventory.append(item)

    def removeItem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False


# Задание 5 — Класс Resistors
class Resistors:
    def __init__(self):
        pass  # Пустой конструктор, чтобы не использовать @staticmethod

    def parallel(self, r1, r2):
        """Общее сопротивление при параллельном соединении двух резисторов."""
        if r1 <= 0 or r2 <= 0:
            raise ValueError("Сопротивления должны быть положительными!")
        return (r1 * r2) / (r1 + r2)

    def consec(self, resistors_list):
        """Общее сопротивление при последовательном соединении."""
        if any(r <= 0 for r in resistors_list):
            raise ValueError("Все сопротивления должны быть положительными!")
        return math.fsum(resistors_list)  # Используем math.fsum из библиотеки math


# Основная программа
if __name__ == "__main__":
    # ===== ЗАДАНИЕ 4 =====
    print("=" * 50)
    print("Практика 7 — Задание 4: Игрок")
    print("=" * 50)
    nick = input("Введите имя игрока: ").strip()
    player = Player(nick)

    while True:
        print("\nВыберите действие:")
        print("1 — Добавить опыт")
        print("2 — Добавить предмет")
        print("3 — Удалить предмет")
        print("4 — Показать данные игрока")
        print("5 — Перейти к заданию 5")
        action = input("Ваш выбор (1–5): ").strip()

        if action == "1":
            try:
                exp = int(input("Сколько опыта добавить? "))
                if exp >= 0:
                    player.addExp(exp)
                    print("Опыт обновлён.")
                else:
                    print("Опыт не может быть отрицательным.")
            except ValueError:
                print("Введите целое число.")

        elif action == "2":
            item = input("Название предмета: ").strip()
            if item:
                player.addItem(item)
                print(f"Предмет '{item}' добавлен в инвентарь.")
            else:
                print("Название не может быть пустым.")

        elif action == "3":
            item = input("Какой предмет удалить? ").strip()
            if player.removeItem(item):
                print(f"Предмет '{item}' удалён.")
            else:
                print("Такого предмета нет в инвентаре.")

        elif action == "4":
            print(player)

        elif action == "5":
            print("Переход к заданию 5...")
            break

        else:
            print("Неверный выбор. Введите число от 1 до 5.")

    # ===== ЗАДАНИЕ 5 =====
    print("\n" + "=" * 50)
    print("Практика 7 — Задание 5: Расчёт сопротивлений")
    print("=" * 50)
    print("1 — Параллельное соединение (2 резистора)")
    print("2 — Последовательное соединение (любое количество)")
    choice = input("Ваш выбор (1 или 2): ").strip()

    calc = Resistors()

    try:
        if choice == "1":
            r1 = float(input("Сопротивление R1 (Ом): "))
            r2 = float(input("Сопротивление R2 (Ом): "))
            total = calc.parallel (r1, r2)
            print(f"Общее сопротивление: {total:.2f} Ом")

        elif choice == "2":
            raw = input("Введите сопротивления через запятую (например: 10, 20, 30): ")
            resistors = [float(x.strip()) for x in raw.split(",")]
            total = calc.consec(resistors)
            print(f"Общее сопротивление: {total:.2f} Ом")

        else:
            print("Неверный выбор. Задание 5 пропущено.")

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")