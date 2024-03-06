class Student:
    students_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.students_list.append(self)
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'
        
    def __average_grade(self):
        total_grades = sum(sum(grades_list) for grades_list in self.grades.values())
        total_courses = sum(len(grades_list) for grades_list in self.grades.values())
        return round(total_grades / total_courses if total_courses else 0, 1)

    def __str__(self) -> str:
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.__average_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress if self.courses_in_progress else '-' )}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses if self.finished_courses else '-' )}\n"
                )
    
    def __eq__(self, __value: object) -> bool:
        return self.__average_grade() == __value.__average_grade()
    
    def __lt__(self, __value: object) -> bool:
        return self.__average_grade() < __value.__average_grade()
    
    def __le__(self, __value: object) -> bool:
        return self.__average_grade() <= __value.__average_grade()

 
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lecturer_list.append(self)

    def __average_grade(self):
        total_grades = sum(sum(grades_list) for grades_list in self.grades.values())
        total_courses = sum(len(grades_list) for grades_list in self.grades.values())
        return round(total_grades / total_courses if total_courses else 0, 1)

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_grade()}\n"
    
    def __eq__(self, __value: object) -> bool:
        return self.__average_grade() == __value.__average_grade()
    
    def __lt__(self, __value: object) -> bool:
        return self.__average_grade() < __value.__average_grade()
    
    def __le__(self, __value: object) -> bool:
        return self.__average_grade() <= __value.__average_grade()


class Reviewer(Mentor):
    reviewer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        Reviewer.reviewer_list.append(self)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'
        
    def __str__(self) -> str:
        return "Имя: {}\nФамилия: {}\n".format(self.name, self.surname)
    

def average_homework_grade_students_course(students, course):
    return round(sum(sum(student.grades.get(course)) / len(student.grades.get(course)) for student in students) / len(students), 1)
   
def average_grade_lecturer(lecturers, course):
    return round(sum(sum(lecturer.grades.get(course)) / len(lecturer.grades.get(course)) for lecturer in lecturers) / len(lecturers), 1)


# Студенты
best_student = Student('Дмитрий', 'Морозов', 'муж.')
best_student.courses_in_progress += ['Python', 'Git']
best_student.add_courses('Введение в программирование')

other_student = Student('Александр', 'Петров', 'муж.')
other_student.courses_in_progress += ['Python', 'Git']
other_student.add_courses('Введение в программирование')
 
# Ревьюеры
cool_reviewer = Reviewer('Северус', 'Снегг')
cool_reviewer.courses_attached += ['Python', 'Git']

smart_reviewer = Reviewer('Майкл', 'Скофилд')
smart_reviewer.courses_attached += ['Python', 'Git']

# Лекторы
cool_lecturer = Lecturer('Эбрагим', 'Аганисян')
cool_lecturer.courses_attached += ['Python', 'Git']

handsome_lecturer = Lecturer('Владимир', 'Путкин')
handsome_lecturer.courses_attached += ['Python', 'Git']

# Оценки, выставленные студентам
cool_reviewer.rate_hw(best_student, 'Python', 10)
smart_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)
smart_reviewer.rate_hw(best_student, 'Git', 9)

cool_reviewer.rate_hw(other_student, 'Python', 10)
smart_reviewer.rate_hw(other_student, 'Python', 9)
cool_reviewer.rate_hw(other_student, 'Git', 10)
smart_reviewer.rate_hw(other_student, 'Git', 9)

# Оценки, выставленные лекторам
best_student.rate_hw(handsome_lecturer, 'Python', 9)
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(handsome_lecturer, 'Git', 10)
best_student.rate_hw(cool_lecturer, 'Git', 10)

other_student.rate_hw(handsome_lecturer, 'Python', 9)
other_student.rate_hw(cool_lecturer, 'Python', 9)
other_student.rate_hw(handsome_lecturer, 'Git', 10)
other_student.rate_hw(cool_lecturer, 'Git', 9)

# Магический метод __str__ для всех классов
print("Ревьюеры:\n" + '\n'.join(map(str, Reviewer.reviewer_list)))
print("Лекторы:\n" + '\n'.join(map(str, Lecturer.lecturer_list)))
print("Студенты:\n" + '\n'.join(map(str, Student.students_list)))

print("Сравнение студентов по средней оценке за домашние задания:")
print(best_student == other_student)
print(best_student > other_student)
print(best_student < other_student)
print(best_student <= other_student)
print(best_student <= other_student, end='\n\n')

print("Сравнение лекторов по средней оценке за лекции:")
print(cool_lecturer == handsome_lecturer)
print(cool_lecturer > handsome_lecturer)
print(cool_lecturer < handsome_lecturer)
print(cool_lecturer <= handsome_lecturer)
print(cool_lecturer <= handsome_lecturer, end='\n\n')

# Средние оценки за домашние задания по всем студентам в рамках конкретного курса
python_grade_students = average_homework_grade_students_course(Student.students_list, 'Python')
git_grade_students = average_homework_grade_students_course(Student.students_list, 'Git')
print(f"Средняя оценка за домашние задания по Python: {python_grade_students}")
print(f"Средняя оценка за домашние задания по Git: {git_grade_students}\n")

# Среднии оценки за лекции всех лекторов в рамках курса
python_grade_lecturer = average_grade_lecturer(Lecturer.lecturer_list, 'Python')
git_grade_lecturer = average_grade_lecturer(Lecturer.lecturer_list, 'Git')
print(f"Средняя оценка за лекции по Python: {python_grade_lecturer}")
print(f"Средняя оценка за лекции по Git: {git_grade_lecturer}")