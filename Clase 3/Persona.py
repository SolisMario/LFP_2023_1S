# class Persona:
#     name = ''
#     department = ''
#     birthday_month = ''

# newPersona = Persona()
# newPersona.name = 'mario'
# newPersona.department = 'Accounting'
# newPersona.birthday_month = 'septiembre'

class Persona:
    def __init__(self, name, department, birthday_month):
        self.name = name
        self.department = department
        self.birthday_month = birthday_month

    def print_name(self):
        print(self.name)