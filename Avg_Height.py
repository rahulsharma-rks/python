height = input("Enter Height of Students:").split()
for i in range(0, len(height)):
    height[i] = int(height[i])
print(height)

total_height = sum(height)

"""for t in height:
    total_height += sum(t)""" 
    
print("Total Height:",total_height)

number_of_students = len(height)
"""
for n in height:
    number_of_students += 1
"""
print("Number of Students:",number_of_students)

avg = round(total_height / number_of_students)
print("Average Height of Student:", avg)