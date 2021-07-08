total_candies = 10
#minimun_candies = 5
number_of_candies = int(input("Enter Number of Candies:"))
if number_of_candies in range(1,6):
    print("Number of Candies Sold:", number_of_candies)
    print("Total Candies:",total_candies - number_of_candies)
else:
    print("Invalid Input!")
    print("Total Candies:",total_candies)
