string1 = input("Enter Your String:")
string2 = input("Enter Character You Want To Search:")
count = 0
for i in string1:
    if i == string2:
        count = count + 1
print("Number of Occurrence of Character",string2,"is",str(count),".")
