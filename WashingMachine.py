weight = int(input("Enter Weight:"))
if (weight == 0):
    print("Time Estimated 0 Minutes.")
elif weight in range(1,2000):
    print("Time Estimated 25 Minutes.")
elif weight in range(2001,4000):
    print("Time Estimated 35 Minutes.")
elif weight in range(4001,7001):
    print("Time Estimated 45 Minutes.")
else:
    print("Invalid Input.")
