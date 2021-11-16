class Person:


    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("My name is " + self.name + " and my age is " + str(self.age))

class Student(Person):


    def __init__(self,name,age,section):
        self.name = name
        self.age = age
        self.section = section

    def displayStudent(self):
        print("My name is " + self.name + " and my age is " + str(self.age) + "my section is" + self.section)



p = Person("Yehonatan",130)

p.display()

s = Student("Liad",24,"Electrical Engineering")

s.display()
s.displayStudent()