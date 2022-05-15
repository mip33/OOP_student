class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if not isinstance(lecturer, Lecturer):
            return 'Лектора нет в списке'
        if course not in self.courses_in_progress or course not in lecturer.courses_attached:
            return "Курс не найден"
        if course in lecturer.rating:
            lecturer.rating[course] += [rate]
        else:
            lecturer.rating[course] = [rate]

    def average_grade(self):
        grades_list = []
        for grade in self.grades.values():
            grades_list += grade
        average_grade = sum(grades_list) / len(grades_list)
        return average_grade

    def __str__(self):
        return (f'Студент \nИмя: {self.name} \nФамилия: {self.surname}'
                f'\nСредняя оценка за домашние задания: {self.average_grade()}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершённые курсы: {", ".join(self.finished_courses)}\n')

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка! Это не студент!'
        else:
            if self.average_grade() > other.average_grade():
                return f'Студент {self.name} {self.surname} успешнее, чем {other.name} {other.surname}\n'
            else:
                return f'Студент {other.name} {other.surname} успешнее, чем {self.name} {self.surname}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating = {}

    def average_rate(self):
        rates_list = []
        for rate in self.rating.values():
            rates_list += rate
        average_rate = sum(rates_list) / len(rates_list)
        return average_rate

    def __str__(self):
        return (f'Лектор \nИмя: {self.name} \nФамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {self.average_rate()}\n')

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка! Это не лектор!'
        else:
            if self.average_rate() > other.average_rate():
                return f'Лектор {self.name} {self.surname} успешнее, чем {other.name} {other.surname}\n'
            else:
                return f'Лектор {other.name} {other.surname} успешнее, чем {self.name} {self.surname}\n'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if not isinstance(student, Student):
            return 'Студента нет в списке'
        if course not in self.courses_attached or course not in student.courses_in_progress:
            return "Курс не найден"
        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]

    def __str__(self):
        return f'Проверяющий \nИмя: {self.name} \nФамилия: {self.surname}\n'


best_student_1 = Student('Иванов', 'Иван', 'boy')
best_student_1.courses_in_progress += ['Python', 'Git']
best_student_2 = Student('Сергеев', 'Сергей', 'boy')
best_student_2.courses_in_progress += ['Python']
best_student_2.finished_courses += ['Git']

reviewer_cool_mentor_1 = Reviewer('Антон', 'Антонов')
reviewer_cool_mentor_1.courses_attached += ['Git']
reviewer_cool_mentor_2 = Reviewer('Елизавета', 'Петровна')
reviewer_cool_mentor_2.courses_attached += ['Python']

lecturer_cool_mentor_1 = Lecturer('Александр', 'Македонский')
lecturer_cool_mentor_1.courses_attached += ['Git']
lecturer_cool_mentor_2 = Lecturer('Марина', 'Петрова')
lecturer_cool_mentor_2.courses_attached += ['Python']

reviewer_cool_mentor_2.rate_hw(best_student_1, 'Python', 7)
reviewer_cool_mentor_1.rate_hw(best_student_1, 'Git', 6)
reviewer_cool_mentor_2.rate_hw(best_student_2, 'Python', 9)

best_student_1.rate_lecturer(lecturer_cool_mentor_2, 'Python', 8)
best_student_1.rate_lecturer(lecturer_cool_mentor_1, 'Git', 6)
best_student_2.rate_lecturer(lecturer_cool_mentor_2, 'Python', 9)

print(best_student_1)
print(best_student_2)
print(reviewer_cool_mentor_1)
print(reviewer_cool_mentor_2)
print(lecturer_cool_mentor_1)
print(lecturer_cool_mentor_2)
print(best_student_1 > best_student_2)
print(lecturer_cool_mentor_2 > best_student_2)
print()


def avg_grades_all(students_list, course):
    all_grades_list = []
    for student in students_list:
        if student.grades.get(course) is not None:
            all_grades_list += student.grades.get(course)
    all_grades_avg = sum(all_grades_list) / len(all_grades_list)
    print(f'Средняя оценка всех студентов за домашние задания по курсу {course}: {all_grades_avg}')


def avg_rates_all(lecturer_list, course):
    all_rates_list = []
    for lecturer in lecturer_list:
        if lecturer.rating.get(course) is not None:
            all_rates_list += lecturer.rating.get(course)
    all_rates_avg = sum(all_rates_list) / len(all_rates_list)
    print(f'Средняя оценка всех лекторов в рамках курса {course}: {all_rates_avg}')


avg_grades_all([best_student_1, best_student_2], 'Python')
avg_grades_all([best_student_1, best_student_2], 'Git')
avg_rates_all([lecturer_cool_mentor_2, lecturer_cool_mentor_1], 'Python')
avg_rates_all([lecturer_cool_mentor_2, lecturer_cool_mentor_1], 'Git')
