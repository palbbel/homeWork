
class Person(object):
    __slots__ = ('__firstname', '__lastname')

    def  __init__(self, firstname, lastname):
        self.__firstname = firstname
        self.__lastname = lastname


    def get_full_name(self):
        return '{} {}'.format(self.get_firstname, self.get_firstname)


    def get_firstname(self):
        return self.__firstname


    def set_firstname(self, firstname):
        self.__firstname = firstname


    def get_lastname(self):
        return self.__lastname


    def set_lastname(self, lastname):
        self.__lastname = lastname


class Course(object):
    __slots__ = ('__name', '__teachers', '__students')
    def __init__(self, name, teachers, students):
        self.__name = name
        self.__teachers = teachers
        self.__students = students

    def get_name_course(self):
        return self.__name


    def set_name_course(self, name):
        self.__name = name


    def get_teachers(self):
        return self.__teachers


    def add_teacher(self, teacher):
        if teacher not in self.get_teachers():
            self.get_teachers().append(teacher)


    def remove_teacher(self, teacher):
        if teacher in self.get_teachers():
            self.get_teachers().remove(teacher)



class Teacher(Person):
    __slots__ = ('__students',)

    def __init__(self, firstname, lastname, students):
        super().__init__(firstname, lastname)
        self.__students = students


    def  add_students(self, student):
        if student not in self.get_students():
            self.get_students().append(student)


    def get_students(self):
        return self.__students


    def remove_student(self, student):
        if student in self.get_students():
            self.get_students().remove(student)


class Student(Person):
    __slots__ = ('__skills',)

    def __init__(self, firstname, lastname, skills):
        super().__init__(firstname, lastname)
        self.__skills = skills


    def  add_skills(self, skill):
        if skill not in self.get_skills():
            self.get_skills().append(skill)


    def get_skills(self):
        return self.__skills


    def remove_skill(self, skill):
        if skill in self.get_skills():
            self.get_skills().remove(skill)


class MyException(Exception):
    pass


if __name__ == '__main__':
    pass
