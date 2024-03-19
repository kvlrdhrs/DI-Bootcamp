class Employee:
    def __init__(self, firstname, lastname, age, job, salary): #attributes
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary
        self.email = f"{firstname.lower()}_{lastname.lowe()}@company.com"


employee1 = Employee('John', 'Doe', 40, 'Front-end Developer', 30000)