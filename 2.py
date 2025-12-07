class StudentGrades:
    def init(self):
        self.grades = []

    def input_grades(self):
        print("Введите 10 оценок студента (от 1 до 12):")
        for i in range(10):
            while True:
                try:
                    grade = int(input(f"Оценка {i + 1}: "))
                    if 1 <= grade <= 12:
                        self.grades.append(grade)
                        break
                    else:
                        print("Ошибка: оценка должна быть от 1 до 12.")
                except ValueError:
                    print("Ошибка: введите целое число.")

    def show_grades(self):
        print(f"\nТекущие оценки: {self.grades}")

    def retake_exam(self):
        try:
            index = int(input("Введите номер оценки для пересдачи (1-10): ")) - 1
            if 0 <= index < len(self.grades):
                new_grade = int(input("Введите новую оценку (1-12): "))
                if 1 <= new_grade <= 12:
                    self.grades[index] = new_grade
                    print(f"Оценка под номером {index + 1} изменена на {new_grade}.")
                else:
                    print("Ошибка: оценка должна быть от 1 до 12.")
            else:
                print("Ошибка: неверный номер оценки.")
        except ValueError:
            print("Ошибка: введите корректное число.")

    def check_pass(self):
        if not self.grades:
            print("Нет оценок для проверки.")
            return
        avg = sum(self.grades) / len(self.grades)
        print(f"\nСредний балл: {avg:.2f}")
        if avg >= 10.7:
            print("✅ Студент выходит!")
        else:
            print("❌ Студент не выходит.")

    def sort_grades(self):
        if not self.grades:
            print("Нет оценок для сортировки.")
            return
        sort_choice = input("Сортировать по возрастанию (a) или убыванию (d)? ").strip().lower()
        if sort_choice == 'a':
            sorted_grades = sorted(self.grades)
            print(f"Отсортировано по возрастанию: {sorted_grades}")
        elif sort_choice == 'd':
            sorted_grades = sorted(self.grades, reverse=True)
            print(f"Отсортировано по убыванию: {sorted_grades}")
        else:
            print("Ошибка: выберите 'a' или 'd'.")

def main():
    student = StudentGrades()
    student.input_grades()

    while True:
        print("\n" + "="*40)
        print("Меню:")
        print("1. Вывод оценок")
        print("2. Пересдача экзамена")
        print("3. Проверить, выходит ли студент")
        print("4. Вывод отсортированного списка оценок")
        print("5. Выход")
        print("="*40)

        choice = input("Выберите действие (1-5): ").strip()

        if choice == '1':
            student.show_grades()
        elif choice == '2':
            student.retake_exam()
        elif choice == '3':
            student.check_pass()
        elif choice == '4':
            student.sort_grades()
        elif choice == '5':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


#MAIN
if name == "main":
    main()
