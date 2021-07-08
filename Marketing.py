parent = input("Enter Parent Name:")
choice = input("Enter Yes/No:")
if choice == 'No' or 'no':
    print("Total Members:1 \n Commission Details: \n{}:250 INR".format(parent))
elif choice == 'Yes' or 'yes':
    child = list(map(str,input("Enter Child Name:").split(",")))
    print("Total Members:{}".format(len(child)+1))
    print("Commission Details:\n{0}{1} INR".format(parent,len(child)*500))
    for i in child:
        print("{0}:250 INR".format(i))