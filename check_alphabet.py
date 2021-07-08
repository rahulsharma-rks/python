c = input("Enter Value:")
if c == '0':
    exit()
elif ((c >= 'a' and  c <= 'z') or (c >= 'A' and  c <= 'Z')):
    print("Alphabet.")
else:
    print("Not Alphabet!")