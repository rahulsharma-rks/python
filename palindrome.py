#NUMBER
number = int(input("Enter Number:"))
temp = number
reverse_num = 0
while(number > 0):
    digit = number % 10
    reverse_num = reverse_num * 10 + digit
    number = number // 10 
if(temp == reverse_num):
    print("Palindrome")
else:
    print("Not Palindrome")

#STRING
def check_palindrome(string):
    length = len(string)
    first = 0
    last = length - 1
    status = 1
    while (first<last):
        if(string[first] == string[last]):
            first = first + 1
            last = last - 1
        else:
            status = 0
            break
    return int(status)
string = input("Enter String:")
status = check_palindrome(string)
if (status):
    print("Palindrome")
else:
    print("Not Palindrome")
