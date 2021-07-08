"""str1 = input("Enter String:")
w = input("Enter Charater to Search:")
if len(str1) > 1:
    for i in range(len(str1)):
        if str1[i] == w:
            print("Character Found.")
            break
        else:
            print("Character Not Found.")
else:
    print("Enter String.")
"""
"""if w in str1:
    print("Chracter Found.")
else:
    print("Character Not Found.")
    """ 

str_1 = input("Enter String:").lower().upper()
str_2 = input("Enter String:").lower().upper()
if(str_1 == str_2):
    print("Strings Matched")
else:
    print("Strings Not Matched")
