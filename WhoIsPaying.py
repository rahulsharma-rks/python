import random
name_list = input("Enter Names of Your Friends:")
names = name_list.split(", ")

len_name_list = len(names)
#print(len_name_list)
random_name = random.randint(0, len_name_list - 1)
print("Friend Who is Going to Buy us Food:",names[random_name])