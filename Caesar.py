#ord: The ord() function returns the number representing the unicode code of a specified character.
#chr:The chr() function returns the character that represents the specified unicode.

def cipher(text,key):
    result = " "
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + key-97) % 26 + 97)
        elif(char.isdigit()):
            result += str(int(char) + key)
        elif(char == '-'):
            result += '-'
        elif (char.isspace()):
            result += " "
    return result

text = input("Enter Text:")
key = int(input("Enter Key:"))
print("Encrypted Message:",cipher(text,key))