class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_sl(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        self.average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self._average_grade() < other._average_grade()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade()}\n\
            Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res


    # def add_courses(self, course_name):
    #     self.finished_courses.append(course_name)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_rating(self):
        self.average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self._average_rating() < other._average_rating()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_rating()}'
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        super().rate_hw(self, student, course, grade)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res



some_student = Student('Ruoy', 'Eman', 'your_gender')
steep_student = Student('Vova', 'Кашин', 'оно')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']
steep_student.courses_in_progress += ['Python']
steep_student.finished_courses += ['Введение в программирование', 'Git']
# cool_mentor.rate_hw(best_student, 'Python', 10)

some_lecturer = Lecturer('Some', 'Buddy')
steep_lecturer = Lecturer('Steep', 'Alex')
some_lecturer.courses_attached += ['Python']
steep_lecturer.courses_attached += ['Python', 'Git']

some_reviewer = Reviewer('Some', 'Buddy')
steep_reviewer = Reviewer('Steep', 'Alex')

some_student.rate_sl(some_lecturer, 'Python', 9)
steep_student.rate_sl(some_lecturer, 'Python', 7)
some_student.rate_sl(steep_lecturer, 'Python', 10 )
some_student.rate_sl(steep_lecturer, 'Python', 10 )
steep_student.rate_sl(steep_lecturer, 'Python', 9)

some_reviewer.rate_hw(some_student, 'Python', 8)
steep_reviewer.rate_hw(some_student, 'Python', 7)
some_reviewer.rate_hw(steep_student, 'Python', 10)
some_reviewer.rate_hw(steep_student, 'Python', 9)
steep_reviewer.rate_hw(steep_student, 'Python', 10)

some_student._average_grade()
steep_student._average_grade()
print(some_student < steep_student)
print(some_student)
print(steep_student)

some_lecturer._average_rating()
steep_lecturer._average_rating()
print(some_lecturer < steep_lecturer)
print(some_lecturer)
print(steep_lecturer)

print(some_reviewer)
print(steep_reviewer)
