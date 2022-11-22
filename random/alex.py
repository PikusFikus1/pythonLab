class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

person = Person()

print(person.name + ' ' + person.surname)