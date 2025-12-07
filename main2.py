import random

class NPC:
    def __init__(self, name: str, hp: int):
        self.__name = name
        self.__hp = hp

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_hp: int):
        if new_hp < 0:
            new_hp = 0
        self.__hp = new_hp

    def __str__(self) -> str:
        return f"Имя: {self.get_name()}, Очки здоровья: {self.get_hp()}"

    def attack(self) -> int:
        # Базовый метод — не должен вызываться напрямую
        return 0


class Swordsman(NPC):
    def __init__(self, name: str, hp: int, min_damage: int, max_damage: int):
        super().__init__(name, hp)
        self.__min_damage = min_damage
        self.__max_damage = max_damage

    def get_min_damage(self):
        return self.__min_damage

    def get_max_damage(self):
        return self.__max_damage

    def attack(self) -> int:
        damage = random.randint(self.get_min_damage(), self.get_max_damage())
        print(f"Мечник {self.get_name()} нанёс {damage} урона!")
        return damage


class Mage(NPC):
    def __init__(self, name: str, hp: int, mana: int):
        super().__init__(name, hp)
        self.__mana = mana

    def get_mana(self):
        return self.__mana

    def set_mana(self, new_mana: int):
        if new_mana < 0:
            new_mana = 0
        self.__mana = new_mana

    def attack(self) -> int:
        if self.get_mana() > 0:
            damage = self.get_mana() * 2  # Урон = удвоенная мана (можно менять)
            self.set_mana(self.get_mana() - 1)
            print(f"Маг {self.get_name()} нанёс {damage} урона!")
            return damage
        else:
            print("Не могу атаковать!")
            return 0


# Пример использования — как в задании
def main():
    # Создаем персонажей
    bilbo = NPC("Бильбо", 15)
    gandalf = Mage("Гендальф", 100, 5)  # Мана = 5
    aragorn = Swordsman("Арагорн", 50, 5, 10)

    # Выводим состояние
    print(bilbo)
    # Попытка атаки NPC (базовый класс)
    bilbo.attack()
    print()

    print(gandalf)
    gandalf.attack()  # Наносит 10 урона (мана=5 → урон=5*2=10)
    print()

    print(aragorn)
    aragorn.attack()  # Случайный урон от 5 до 10
    print()

    print(gandalf)
    # Атакуем ещё раз — мана уменьшается
    gandalf.attack()  # Урон = 8 (мана=4 → 4*2=8)
    print()

    print(gandalf)
    # Используем ману до конца
    for _ in range(3):
        gandalf.attack()
    print()

    # кончилась мана
    print(gandalf)
    gandalf.attack()  # "Не могу атаковать!"


if __name__ == "__main__":
    main()