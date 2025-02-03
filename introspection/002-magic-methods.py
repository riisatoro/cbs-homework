# Завдання 2
#
# Створити клас Contact з полями surname, name, age, mob_phone, email. 
# Додати методи get_contact, sent_message. Створити клас-нащадок UpdateContact 
# з полями surname, name, age, mob_phone, email, job. Додати методи get_message. 
# Створити екземпляри класів та дослідити стан об'єктів за допомогою
#  атрибутів: __dict__, __base__, __bases__. Роздрукувати інформацію на екрані.

class Contact:
    def __init__(self, name: str, surname: str, age: int, mob_phone: str, email: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.mob_phone = mob_phone
        self.email = email
    
    def get_contact(self) -> str:
        return self.mob_phone

    def send_message(self):
        print("Sending message to {self.email}")


class UpdateContact(Contact):
    def __init__(self, job, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job

    def get_message(self):
        return "Message"


contact = Contact("Alex", "Jonson", 26, "+39088777665", "admin@admin.com")
update_contact = UpdateContact("manager", "John", "Doe", 35, "+374635242", "test@test.com")

print(contact.__dict__)
print(update_contact.__dict__)

print(Contact.__base__)
print(UpdateContact.__base__)

print(Contact.__bases__)
print(UpdateContact.__bases__)


# Завдання 3
#
# Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr(). 
# Застосувати ці функції до кожного з атрибутів класів, подивитися до чого це призводить.


print(hasattr(contact, "job"))
print(hasattr(update_contact, "job"))

setattr(update_contact, "company_name", "BigTech")
print(getattr(update_contact, "company_name"))

delattr(update_contact, "company_name")
print(hasattr(update_contact, "company_name"))


# Завдання 4

# Використовуючи код з завдання 2, створити 2 екземпляри обох класів. 
# Використати функції isinstance() – для перевірки екземплярів класу (за яким класом створені) та 
# issubclass() – для перевірки і визначення класу-нащадка.

print(isinstance(contact, Contact))
print(isinstance(update_contact, Contact))

print(isinstance(contact, UpdateContact))
print(isinstance(update_contact, UpdateContact))

print(issubclass(Contact, UpdateContact))
print(issubclass(UpdateContact, Contact))


# Завдання 5

# Використовуючи код завдання 2 надрукуйте у терміналі інформацію, 
# яка міститься у класах Contact та UpdateContact та їх екземплярах. 
# Видаліть атрибут job, і знову надрукуйте стан класів та їх екземплярів. 
# Порівняйте їх. Зробіть відповідні висновки.

print(dir(contact), dir(update_contact))

delattr(update_contact, "job")
print(dir(contact), dir(update_contact))

# 6
#
# Використовуючи код завдання 2 надрукуйте у терміналі всі методи, які містяться у класі Contact та UpdateContact.

for attr in dir(contact):
    if callable(getattr(contact, attr)):
        print("Method: ", attr)
