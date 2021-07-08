class  Error(Exception):
    pass
class dobException(Error):
    pass

year = int(input("Enter Year of Birth:"))
age = 2021 - year
try:
    if age<=30 and age>20:
        print("Age is Valid.")
    else:
        raise dobException 
except dobException:
    print("Age is Not Valid.")