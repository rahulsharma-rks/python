"""
A Class is like an object constructor, or a "blueprint" for creating objects.
All classes have a function called __init__(), which is always executed when the class is being initiated. 

"""


class Person:
    def __init__(self, fname, sname, age):
        self.fname = fname
        self.sname = sname
        self.age = age

p1 = Person("Rahul","Sharma","24")
print(p1.fname,p1.sname,p1.age)

