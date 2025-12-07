import random

# Задание 1:
class SimpleStatistics:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        freq = {}
        for x in self.data:
            freq[x] = freq.get(x, 0) + 1
        max_count = max(freq.values())
        return [k for k, v in freq.items() if v == max_count]

    def range(self):
        return max(self.data) - min(self.data)

    def variance(self):
        m = self.mean()
        return sum((x - m) ** 2 for x in self.data) / (len(self.data) - 1)

    def standard_deviation(self):
        return self.variance() ** 0.5


# Задание 2:
class FrequencyDistribution:
    def __init__(self, data):
        self.data = data

    def calculate_frequencies(self):
        freq = {}
        for x in self.data:
            freq[x] = freq.get(x, 0) + 1
        return freq

    def display_frequency_table(self):
        print("Значение | Частота")
        print("-" * 15)
        for val, count in self.calculate_frequencies().items():
            print(f"{val:7} | {count}")

    def get_most_frequent(self):
        freq = self.calculate_frequencies()
        max_count = max(freq.values())
        return [k for k, v in freq.items() if v == max_count]


# Задание 3:
class Correlation:
    def __init__(self, X, Y):
        if len(X) != len(Y):
            raise ValueError("Списки должны быть одинаковой длины")
        self.X = X
        self.Y = Y

    def pearson_correlation(self):
        n = len(self.X)
        sum_x = sum(self.X)
        sum_y = sum(self.Y)
        sum_xy = sum(x * y for x, y in zip(self.X, self.Y))
        sum_x2 = sum(x ** 2 for x in self.X)
        sum_y2 = sum(y ** 2 for y in self.Y)

        numerator = n * sum_xy - sum_x * sum_y
        denominator = ((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)) ** 0.5
        if denominator == 0:
            return 0
        return numerator / denominator


# Задание 4:
class HypothesisTest:
    def run_test(self):
        pass

    def get_p_value(self):
        return 0.05  # заглушка

    def interpret_results(self, alpha=0.05):
        p = self.get_p_value()
        if p < alpha:
            return "Отклоняем гипотезу"
        else:
            return "Не отклоняем гипотезу"


class TTest(HypothesisTest):
    def __init__(self, data1, data2=None):
        self.data1 = data1
        self.data2 = data2

    def run_test(self):
        print("Запуск t-теста (упрощённо)")


class ChiSquareTest(HypothesisTest):
    def __init__(self, table):
        self.table = table

    def run_test(self):
        print("Запуск хи-квадрат теста (упрощённо)")


# Задание 5:
class LinearRegression:
    def __init__(self):
        self.slope = 0
        self.intercept = 0

    def fit(self, X, y):
        n = len(X)
        sum_x = sum(X)
        sum_y = sum(y)
        sum_xy = sum(x * y for x, y in zip(X, y))
        sum_x2 = sum(x ** 2 for x in X)

        self.slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        self.intercept = (sum_y - self.slope * sum_x) / n

    def predict(self, X):
        return [self.slope * x + self.intercept for x in X]

    def evaluate(self, X, y):
        y_pred = self.predict(X)
        mse = sum((true - pred) ** 2 for true, pred in zip(y, y_pred)) / len(y)
        return {"MSE": mse}


# Задание 6:
class Sampling:
    @staticmethod
    def simple_random_sample(data, n):
        return random.sample(data, n)

    @staticmethod
    def systematic_sample(data, k):
        return data[::k]


# Задача 6:
class RealString:
    def __init__(self, s):
        self.s = str(s)

    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self.s) == len(other.s)
        elif isinstance(other, str):
            return len(self.s) == len(other)
        return False

    def __lt__(self, other):
        if isinstance(other, RealString):
            return len(self.s) < len(other.s)
        elif isinstance(other, str):
            return len(self.s) < len(other)
        return NotImplemented

    def __gt__(self, other):
        return not (self < other or self == other)


# Задача 7*:
class Game15:
    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.empty = [2, 2]
        self.shuffle(20)

    def shuffle(self, steps):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for _ in range(steps):
            valid = []
            r, c = self.empty
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 3 and 0 <= nc < 3:
                    valid.append((nr, nc))
            if valid:
                nr, nc = random.choice(valid)
                self.board[r][c], self.board[nr][nc] = self.board[nr][nc], self.board[r][c]
                self.empty = [nr, nc]

    def print_board(self):
        for row in self.board:
            print(" ".join(str(x) if x != 0 else "." for x in row))

    def is_solved(self):
        target = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == target


# Задача 8*:
def simulate_powerball(my_numbers, my_powerball, simulations=100000):
    wins = 0
    for _ in range(simulations):
        draw = random.sample(range(1, 70), 5)
        pb = random.randint(1, 26)
        if set(draw) == set(my_numbers) and pb == my_powerball:
            wins += 1
    print(f"Симуляция {simulations} розыгрышей завершена.")
    print(f"Совпадений: {wins} (шанс ≈ {wins / simulations:.6f})")


# Примеры использования
if __name__ == "__main__":
    stats = SimpleStatistics([1, 2, 2, 3, 4])
    print("Среднее:", stats.mean())
    print("Медиана:", stats.median())
    print("Мода:", stats.mode())

    s1 = RealString("Привет")
    s2 = RealString("Hello")
    print(s1 == s2)
