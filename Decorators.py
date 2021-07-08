#Function Copy
"""def welcome():
    return "Welcome Python"

wel = welcome()
#del welcome
print(wel)"""

#Closure: function inside function
"""def main_welcome():
    msg = "Hello"
    def sub_welcome():
        print("Python")
        print(msg)
    return sub_welcome()
print(main_welcome())"""

#Decorator
def main_welcome():
    msg = "Hello"
    def sub_welcome():
        print("Python")
        print(msg)
    return sub_welcome()
#print(main_welcome())

@main_welcome()
def code():
    print("Python Code")
    return code()

a=main_welcome(code)
print(a)