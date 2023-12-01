class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашнее задание: {calculate_average_grade(self.grades)}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        return calculate_average_grade(self.grades) < calculate_average_grade(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {calculate_average_grade(self.grades)}")

    def __lt__(self, other):
        return calculate_average_grade(self.grades) < calculate_average_grade(other.grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


# Расчитаем среднюю оценку,как для студента,так и для лектора
def calculate_average_grade(grades):
    len_ = 0
    sum_ = 0
    for grade in grades.values():
        sum_ += sum(grade)
        len_ += len(grade)
    return round(sum_ / len_, ndigits=1)


# Расчитаем среднюю оценку для всех студентов и лекторов

def calculate_average_course_grade(list_person, course):
    len_ = 0
    sum_ = 0
    for person in list_person:
        sum_ += sum(person.grades[course])
        len_ += len(person.grades[course])
    return round(sum_ / len_, ndigits=1)


# Зададим параметры для первого студента

student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ["Введение в программирование"]

# Зададим параметры для второго студента

student_2 = Student('Duoy', 'Iman', 'your_gender')
student_2.courses_in_progress += ['Python', 'Git']

# Зададим параметры для проверяющего

cool_reviewer = Reviewer('Some', "Buddy")
cool_reviewer.courses_attached += ['Python', 'Git']

# Проверяющий ставит оценки 1 и 2 студенту по курсу "Python"

cool_reviewer.rate_hw(student_1, 'Python', 10)
cool_reviewer.rate_hw(student_2, 'Python', 5)

# Проверяющий ставит оценки 1 и 2 студенту по курсу "Git"

cool_reviewer.rate_hw(student_1, 'Git', 8)
cool_reviewer.rate_hw(student_2, 'Git', 6)

# Зададим параметры лектору

lecturer_1 = Lecturer('Some', "Buddy")
lecturer_1.courses_attached += ['Python', 'Git']

# Студент оценивает лектора по курсам
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'Git', 9)

# Зададим параметры второму лектору

lecturer_2 = Lecturer('Some', "Buddy")
lecturer_2.courses_attached += ['Python', 'Git']

# Cтудент оценивает второго лектора

student_1.rate_lecturer(lecturer_2, 'Python', 4)
student_1.rate_lecturer(lecturer_2, 'Git', 6)

print(cool_reviewer)
print()
print(lecturer_1)
print()
print(student_1)
print()

# Вывод сравнения сравнения средних оценок лекторов и студентов
print("Сравнение оценок студентов:")
print(student_1 < student_2)
print("Сравнение оценок лекторов:")
print(lecturer_1 < lecturer_2)
print()

# Вывод средних оценок студентов и лекторов
print("Вывод средних оценок студентов")
print(calculate_average_grade(student_1.grades))
print(calculate_average_grade(student_2.grades))
print("Вывод средних оценок лекторов")
print(calculate_average_grade(lecturer_1.grades))
print(calculate_average_grade(lecturer_2.grades))
print()

# Вывод средних оценок между лекторами
print("Вывод средней оценки между лекторами по курсу 'Git'")
print(calculate_average_course_grade([lecturer_1, lecturer_2], "Git"))
print("Вывод средней оценки между лекторами по курсу 'Python'")
print(calculate_average_course_grade([lecturer_1, lecturer_2], "Python"))
print()

# Вывод средних оценок между студентами
print("Вывод средней оценки между студентами по курсу 'Git'")
print(calculate_average_course_grade([student_1, student_2], "Git"))
print("Вывод средней оценки между студентами по курсу 'Python'")
print(calculate_average_course_grade([student_1, student_2], "Python"))
