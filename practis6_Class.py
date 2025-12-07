import random

class Searcher:
    def __init__(self):
        self.numbers = [random.randint(1, 50) for _ in range(10)]
        print(f"Исходный список: {self.numbers}")

    def linear_search(self, target):
        # Линейный поиск
        for i, num in enumerate(self.numbers):
            if num == target:
                return i
        return -1

    def binary_search(self, target):
        # Бинарный поиск
        sorted_numbers = sorted(self.numbers)
        print(f"Отсортированный список для бинарного поиска: {sorted_numbers}")

        left = 0
        right = len(sorted_numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_numbers[mid] == target:
                return mid
            elif sorted_numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def get_user_input(self):
        while True:
            try:
                user_input = input("Введите число для поиска: ").strip()
                if not user_input:
                    print("Ошибка: введите число.")
                    continue
                if '.' in user_input:
                    target = float(user_input)
                else:
                    target = int(user_input)
                return target
            except ValueError:
                print("Ошибка: введите корректное число (целое или дробное).")

    def run(self):
        target = self.get_user_input()
        print(f"\nИщем число: {target}\n")

        print("--- Задание 1: Линейный поиск ---")
        index_linear = self.linear_search(target)
        if index_linear != -1:
            print(f"Число {target} найдено на позиции {index_linear} (индексация с 0).")
        else:
            print(f"Число {target} не найдено в списке.")

        print("\n--- Задание 2: Бинарный поиск ---")
        index_binary = self.binary_search(target)
        if index_binary != -1:
            print(f"Число {target} найдено на позиции {index_binary} в отсортированном списке.")
        else:
            print(f"Число {target} не найдено в отсортированном списке.")


class Soda:
    def __init__(self, additive=None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print("Обычная газировка")


def get_additive_input():
    additive = input("Введите добавку для газировки (или нажмите Enter для обычной газировки): ").strip()
    return additive if additive else None


if __name__ == "__main__":
    searcher = Searcher()
    searcher.run()

    print("\n--- Задание 3: Класс Soda ---")
    additive = get_additive_input()
    soda = Soda(additive)
    soda.show_my_drink()