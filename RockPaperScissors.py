import random
print("/***Rock Paper Scissors***/")
rock = '''
//ROCK//
'''
paper = '''
///PAPER///
'''
scissor = '''
////SCISSORS////
'''
game_image = [rock, paper, scissor]

user_choice = int(input("What do you choose?\n Type 0 for Rock \n 1 for Paper \n 2 for Scissors\n"))

if user_choice >= 3 or user_choice < 0:
    print("Invalid Input. You Lose!")
else:
    print("User's Choice:",game_image[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer's Choice is:",game_image[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("It's Draw!")
