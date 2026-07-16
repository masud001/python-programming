from unicodedata import name


class Employee:

    company = "masud"

    def __init__(self, name, salary, age):
        self.name = name
        self.age = age
        self.salary = salary

    @property
    def email(self):
        return f"{self.name}@{self.__class__.company.lower()}.com"

    # def generate_email(self, cls):
    #     return f"{self.name}@{cls.company}.com"

    def show_info(self):
        info = f"Name: {self.name} | Age: {self.age} | Salary: {self.salary} | Email: {self.email}"
        print(info)


    @classmethod
    def update_company_name(cls, new_name):
        cls.company = new_name



class B(Employee):
    def method1(self):
        print("Hello World B Class Method 1")
    def method2(self):
        print("Hello World B Class Method 2")




Employee.update_company_name("MasudCompany")
obj = Employee("Masudur", 5000, 30)
obj.show_info()

# B.update_company_name("mmCompany")
b= B("Masud", 6000, 40)
b.update_company_name("jayaCompany")
b.show_info()