class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method
P1 = Person("Rahul","Sharma")
P1.printname()
