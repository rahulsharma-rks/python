#Rock beats scissors
#Scissors beats paper
#Paper beats rock



user_1 = input("Enter 1st Player Name:")
user_2 = input("Enter 2nd Player Name:")

user_1_answer = input("%s, Do you want Rock, Paper or Scissor?" %user_1)
user_2_answer = input("%s, Do you want Rock, Paper or Scissor?" %user_2)

def compare(u1,u2):
    if u1 == u2:
        print("Its a Tie")
    elif u1 == 'Rock':
        if u2 == 'Scissor':
            print("Rock Wins!")
        else:
            print("Paper Wins!")
    elif u1 == 'Scissor':
        if u2 == 'Paper':
            print("Scissor Wins!")
        else:
            print("Rock Wins!")
    elif u1 == 'Paper':
        if u2 == 'Rock':
            print("Paper Wins!")
        else:
            print("Scissor Wins!")
    else:
        print("Invalid Input!!!!!")


print(compare(user_1_answer,user_2_answer))
