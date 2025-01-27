# Завдання 5
# 
# Використовуючи код example_10, створіть декоратор @staticmethod 
# для визначення повноліття людини в Україні та Америки.
#
#
# Завдання 6
#
# 


from datetime import date


AGE_RESTRICTIONS_UNTIL = {
    "usa": 21,
    "ua": 18,
}


class MyClass1:
    people_above_age_limits = 0

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear, country_code: str = "usa"):
        age = date.today().year - birthYear
        if MyClass1.has_age_restrictions(country_code="usa", age=age):
            cls.people_above_age_limits += 1

        return cls(surname, name, age)

    @staticmethod
    def has_age_restrictions(self, country_code: str, age: int):
        country_code = country_code.lower()
        if country_code not in AGE_RESTRICTIONS_UNTIL:
            print(f"Can't find ruling for this country: {country_code}")
        
        if AGE_RESTRICTIONS_UNTIL[country_code] < age:
            print("User is restricted to some content")
        else:
            print("User can view any type of content")

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))


class MyClass2(MyClass1):
    color = 'White'


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per1.print_info()

m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan',  2005)
m_per2.print_info()

m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
print(isinstance(m_per3, MyClass2))

m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001)
print(isinstance(m_per4, MyClass1))

print(issubclass(MyClass1, MyClass2))
print(issubclass(MyClass2, MyClass1))

MyClass1.has_age_restrictions("usa", 20)
MyClass1.has_age_restrictions("usa", 25)

MyClass1.has_age_restrictions("ua", 21)
MyClass1.has_age_restrictions("usa", 17)

MyClass1.has_age_restrictions("n/a", 25)

print("People above age restiction: ", MyClass1.people_above_age_limits)
