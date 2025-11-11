class Employee:
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        return 5000

class Developer(Employee):
    def calculate_salary(self):
        return 4000

staff = [Manager(), Developer()]
for person in staff:
    print("Salary:", person.calculate_salary())
