
import random
user = input("Rock(r), Paper(p), or Scissors(s)?: ")

l = ['r', 'p', 's']
computer = random.choice(l)

print("Computer's play is: ", computer)

if (user == 'r') and (computer == 's'):

    print("winner winner chicken dinner!")

elif (user == 'r') and (computer == 'p'):

    print("Opps you failed this time ,try again!")

elif (user == 'r') and (computer == 'r'):

    print("Oooh no one wins, try again?")

elif (user == 'p') and (computer == 's'):

    print("Oops computer cuts your paper! try again until you win")

elif (user == 'p') and (computer == 'r'):

    print("Winner Winner Chicken Dinner!")

elif (user == 'p') and (computer == 'p'):
    
    print("Oooh no one wins, try again?")

elif (user == 's') and (computer == 'r'):

    print("Oops computer's rock destroy your scissors!, try again")

elif (user == 's') and (computer == 'p'):

    print("great play! your scissors cut computer's paper")

else:

    print("Oooh no one wins, try again?")
