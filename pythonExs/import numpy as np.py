class Person:
    def __init__(self, name, age, horoscope):  # constructor(__init__)
        self.name = name
        self.age = age
        self.horoscope = horoscope

    def greet(self, another_person=None):
        if another_person is None:
            print("Hello! My name is", self.name)
            print("I am", self.age)
            print("My sign is", self.horoscope)
        else:
            print("Hello!", another_person.name,
                  "My name is", self.name)
            print("I am", self.age)

    def grow(self):
        self.age = self.age + 1

    def __rep__(self):
        return "A person whose name is " + self.name

    def __eq__(self, other):
        return self.name == other.name and \
            self.age == other.age and \
            self.horoscope == other.horoscope


class Student(Person):
    def __init__(self, name, age, horoscope, subject):
        super().__init__(name, age, horoscope)
        self.subject = subject

    def greet(self):
        super().greet()
        print("I am studying", self.subject)


Lis = Student("Lis", 19, "Virgo", "EEE")
print(Lis)
Lis.greet()
