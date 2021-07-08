try:
    """a = 1
    b = "S"
    c = a+b"""
    a = int(input("Number1:"))
    b = int(input("Number2:"))
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    """print("Sum:",sum)
    print("Sub:",sub)
    print("Mul:",mul)
    print("Div:",div)"""
#Child Class: NameError,TypeError,ZeroDivisionError

except NameError:
    print("User Have Not Defined Variable.")
except ZeroDivisionError:
    print("Enter Number Greater Than 0.")
except TypeError:
    print("Unsupported Type Error.Try To Make Data Type Similar.")
#Generic Class Name
except Exception as ex:
    print(ex)
else:
    print("Sum:",sum)
    print("Sub:",sub)
    print("Mul:",mul)
    print("Div:",div)

finally:
    print("Execution is Complete.")