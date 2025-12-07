from abc import ABC, abstractmethod

# Задание 1:
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Задание 2:
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Woof!")

    def eat(self):
        print("Собака ест корм.")


class Cat(Animal):
    def make_sound(self):
        print("Мяу!")

    def eat(self):
        print("Кот ест рыбу.")


class Bird(Animal):
    def make_sound(self):
        print("Чирик!")

    def eat(self):
        print("Птица клевала зёрнышки.")


# Задание 3:
class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund_payment(self, payment_id, amount):
        pass


class PayPalPayment(PaymentSystem):
    def __init__(self, api_key):
        self.api_key = api_key

    def process_payment(self, amount):
        print(f"PayPal: платёж на {amount} обработан.")

    def refund_payment(self, payment_id, amount):
        print(f"PayPal: возврат {amount} по платежу {payment_id}.")


class StripePayment(PaymentSystem):
    def __init__(self, api_key):
        self.api_key = api_key

    def process_payment(self, amount):
        print(f"Stripe: платёж на {amount} обработан.")

    def refund_payment(self, payment_id, amount):
        print(f"Stripe: возврат {amount} по платежу {payment_id}.")


# Задание 4:
class OrderProcessor(ABC):
    @abstractmethod
    def validate_order(self, order):
        pass

    @abstractmethod
    def calculate_total(self, order):
        pass

    @abstractmethod
    def process_payment(self, order):
        pass

    @abstractmethod
    def ship_order(self, order):
        pass


class StandardOrderProcessor(OrderProcessor):
    def validate_order(self, order):
        if "items" not in order or not order["items"]:
            print("Ошибка: заказ пуст.")
            return False
        return True

    def calculate_total(self, order):
        return sum(item["price"] * item["qty"] for item in order["items"])

    def process_payment(self, order):
        print("Обычная оплата...")

    def ship_order(self, order):
        print("Доставка обычной почтой.")


class PremiumOrderProcessor(OrderProcessor):
    def validate_order(self, order):
        if not order.get("is_vip"):
            print("Ошибка: премиум-заказ только для VIP.")
            return False
        return True

    def calculate_total(self, order):
        total = sum(item["price"] * item["qty"] for item in order["items"])
        return total * 0.9  # скидка 10%

    def process_payment(self, order):
        print("Премиум-оплата (ускоренная)...")

    def ship_order(self, order):
        print("Экспресс-доставка!")


# Примеры
if __name__ == "__main__":
    c = Circle(5)
    r = Rectangle(4, 6)
    print("Круг: площадь =", c.area(), "периметр =", c.perimeter())
    print("Прямоугольник: площадь =", r.area(), "периметр =", r.perimeter())

    for animal in [Dog(), Cat(), Bird()]:
        animal.make_sound()
        animal.eat()

    order = {
        "items": [{"name": "Книга", "price": 300, "qty": 2}],
        "is_vip": True
    }

    std = StandardOrderProcessor()
    prem = PremiumOrderProcessor()

    print("Стандарт:", std.calculate_total(order))
    print("Премиум:", prem.calculate_total(order))