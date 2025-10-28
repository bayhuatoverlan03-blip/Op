class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, value):
        if 0 <= value <= 4:
            self.__gpa = value
        else:
            print("Invalid GPA value")


class Course:
    def __init__(self, title, credits):
        self._title = title
        self._credits = credits

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, value):
        if value <= 0:
            raise ValueError("Credits must be positive")
        self._credits = value


class OnlineCourse(Course):
    def add_bonus(self, extra):
        self.credits += extra


st = Student("Aruzhan", 3.6)
st.set_gpa(3.9)
print(st.get_gpa())

c = Course("Python Programming", 3)
print(c.credits)
c.credits = 4
print(c.credits)

oc = OnlineCourse("Data Science", 5)
oc.add_bonus(1)
print(oc.credits)