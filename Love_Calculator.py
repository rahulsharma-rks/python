print("Find Your Destiny!")
name1 = input("Enter Your Name: \n").lower()
name2 = input("Enter His/Her Name: \n").lower()
combined_string = name1 + name2

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

true = t + r + u + e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

love = l + o + v + e

score = int(str(true + love))

if (score < 10) or (score > 90):
    print(f"You Love Score is {score}.")
elif (score >= 40) and (score <= 50):
    print(f"You Love Score is {score}.")
else:
    print(f"You Love Score is {score}.")