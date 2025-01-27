# Завдання 1
#
# Створіть клас Editor, який містить методи view_document та edit_document. 
# Нехай метод edit_document виводить на екран інформацію про те, 
# що редагування документів недоступне для безкоштовної версії. 
# Створіть підклас ProEditor, у якому цей метод буде перевизначено. 
# Введіть ліцензійний ключ із клавіатури і, якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor. 
# Викликайте методи перегляду та редагування документів.


COMMUNITY_LICENSE = "community"
PRO_LICENSE = "pro"

class Editor:
    def __init__(self, user_email: str):
        self.user_email = user_email
    
    def view_document(self, document: str):
        print(f"User {self.user_email} is viewing the {document} document")
    
    def edit_document(self, document: str):
        print(f"You can't edit {document} in community version. Consider upgrading to PRO.")


class ProEditor(Editor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def edit_document(self, document: str):
        print(f"User {self.user_email} is editing the {document} document.")


user_key = input("Enter your license: ")
user_email = input("Enter your email: ")

editor = None

if user_key == COMMUNITY_LICENSE:
    editor = Editor(user_email)
elif user_key == PRO_LICENSE:
    editor = ProEditor(user_email)

if editor is not None:
    editor.view_document("Book of things")
    editor.edit_document("Book of things")
else:
    print("Invalid license key")
