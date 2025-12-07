import random

# Практика 7 — Задание 1: Животные
class Animal:
    def __init__(self, nickname):
        self.nickname = nickname
    def __str__(self):
        return self.nickname

class Cat(Animal):
    def voice(self):
        print(f"{self.nickname}: Мяу!")
    def run(self):
        print("Побежали!")

class Parrot(Animal):
    def __init__(self, nickname, can_talk=False):
        super().__init__(nickname)
        self.can_talk = can_talk

    def voice(self):
        if self.can_talk:
            print(f"{self.nickname}: Чирик-чирик, привет!")
        else:
            print(f"{self.nickname}: Чирик-чирик!")

    def fly(self):
        print("Полетели!")


# Практика 7 — Задание 2: Сообщения

class Message:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient

    def showHeader(self):
        print(f"От: {self.sender} → Для: {self.recipient}")


class TextMessage(Message):
    def __init__(self, sender, recipient, text):
        super().__init__(sender, recipient)
        self.text = text

    def send(self):
        self.showHeader()
        print("Текст сообщения:")
        print(self.text)


class StickerMessage(Message):
    STICKERS = [
        "ʕ•ᴥ•ʔ",
        "( ͡° ͜ʖ ͡°)",
        "(ง’̀-‘́)ง",
        "(ʘ‿ʘ)",
        "(✿◠‿◠)",
        "^._.^"
    ]

    def __init__(self, sender, recipient, sticker_index):
        super().__init__(sender, recipient)
        self.sticker = self.STICKERS[sticker_index]
        self.count = 1

    def send(self):
        self.showHeader()
        print(f"Стикер отправлен с радостью! {self.sticker} (уже отправляли {self.count} раз!)")
        self.count += 1


# Практика 7 — Задание 3: Игральные кости (MSDice)

class MSDice:
    def __init__(self, sides):
        if sides not in [4, 6, 10, 20]:
            raise ValueError("Поддерживаются только кубики: D4, D6, D10, D20")
        self.sides = sides
        self.value = None

    def roll(self):
        self.value = random.randint(1, self.sides)
        return self.value

    def __str__(self):
        return f"D{self.sides}: выпало {self.value}"


# Основная программа

if __name__ == "__main__":
    # ============== ЗАДАНИЕ 1 ==============
    print("=" * 50)
    print("Практика 7 — Задание 1: Животные")
    print("=" * 50)

    print("Выберите тип животного:")
    print("1 — Кот")
    print("2 — Попугай")

    choice = input("Ваш выбор (1 или 2): ").strip()
    nickname = input("Введите кличку животного: ").strip()

    if choice == "1":
        animal = Cat(nickname)
        animal.voice()
        animal.run()
    elif choice == "2":
        talk_choice = input("Попугай говорящий? (да/нет): ").strip().lower()
        can_talk = talk_choice in ("да", "д", "yes", "y")
        animal = Parrot(nickname, can_talk=can_talk)
        animal.voice()
        animal.fly()
    else:
        print("Неверный выбор. Переходим к следующему заданию.")

    # ============== ЗАДАНИЕ 2 ==============
    print("\n" + "=" * 50)
    print("Практика 7 — Задание 2: Сообщения")
    print("=" * 50)

    sender = input("Введите ваше имя (отправитель): ").strip()
    recipient = input("Кому отправить сообщение (получатель): ").strip()

    print("\nВыберите тип сообщения:")
    print("1 — Текстовое сообщение")
    print("2 — Стикер")

    msg_type = input("Ваш выбор (1 или 2): ").strip()

    if msg_type == "1":
        text = input("Введите текст сообщения: ").strip()
        msg = TextMessage(sender, recipient, text)
        print("\n📤 Отправка текстового сообщения:\n")
        msg.send()
    elif msg_type == "2":
        print("\nДоступные стикеры:")
        for i, sticker in enumerate(StickerMessage.STICKERS):
            print(f"{i + 1}. {sticker}")

        while True:
            try:
                choice = int(input(f"\nВыберите номер стикера (1–{len(StickerMessage.STICKERS)}): "))
                if 1 <= choice <= len(StickerMessage.STICKERS):
                    sticker_index = choice - 1
                    break
                else:
                    print("Пожалуйста, введите номер из списка.")
            except ValueError:
                print("Введите целое число!")

        msg = StickerMessage(sender, recipient, sticker_index)
        print("\n📤 Отправка стикера:\n")
        msg.send()
    else:
        print("Неверный выбор. Переходим к следующему заданию.")

    # ============== ЗАДАНИЕ 3 ==============
    print("\n" + "=" * 50)
    print("Практика 7 — Задание 3: Игральные кости (MSDice)")
    print("=" * 50)

    print("Доступные кубики:")
    print("D4 — 4 грани")
    print("D6 — 6 граней")
    print("D10 — 10 граней")
    print("D20 — 20 граней")

    while True:
        try:
            sides = int(input("\nВыберите количество граней кубика (4, 6, 10 или 20): "))
            if sides in [4, 6, 10, 20]:
                break
            else:
                print("Пожалуйста, введите одно из значений: 4, 6, 10, 20.")
        except ValueError:
            print("Введите целое число!")

    while True:
        try:
            rolls = int(input("Сколько раз бросить кубик? (целое число ≥1): "))
            if rolls >= 1:
                break
            else:
                print("Число бросков должно быть ≥1.")
        except ValueError:
            print("Введите целое число!")

    dice = MSDice(sides)
    print(f"\nБросаем кубик D{sides} {rolls} раз(а):")
    for i in range(rolls):
        result = dice.roll()
        print(f"Бросок {i + 1}: {result}")