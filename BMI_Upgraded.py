weight = input("Enter Weight in KG:")
height = input("Enter Height in m:")
bmi = round(weight / height ** 2)

print("BMI:", int(bmi)) 
if bmi < 18.5:
    print(f"Your BMI is {bmi}, Underweight!")
elif bmi < 25:
    print(f"Your BMI is {bmi},Normal Weight")
elif bmi < 30:
    print(f"Your BMI is {bmi},Over Weight") 
elif bmi < 35:
    print(f"Your BMI is {bmi},Obese")
else:
    print(f"Your BMI is {bmi},Clinically Obese")