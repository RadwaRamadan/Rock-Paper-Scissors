'''
    Basic idea : 
        1-Store the three cases in a dictionary 
        2-Get the input from the user
        3-Generate a random integer representing the computer choice
        4-Compare the the user choice and the computer choice as follow :
            4.1-computer chooses the same as the user
            4.2-The computer chooses different choice than the user
                4.2.1-Choice_1 = Scissor , Choice_2 = paper ==> Scissor win
                4.2.2-Choice_1 = Scissor , Choice_2 = Rock  ==> Rock wins
                4.2.3-Choice_1 = paper   , Choice_2 = Rock  ==> Paper wins
        5-Declare the winner according to the rules in step 4.

'''

from random import randint

options = {1:'Rock',2:'Paper',3:'Scissor'}

user_choice = int(input("Your_Choice[1-3] :"))
if user_choice<1 or user_choice >3:
    print("Invalid Choice")
computer_choice = randint(1,3)

## compare the two choices
## if the same or not (if not further check nedded,if the same repeat the geame)
winner_choice=''
if computer_choice==user_choice:
    print("DRAW")
else:
    if (options[computer_choice]=='Rock' and options[user_choice]=='Paper') or (options[computer_choice]=='Paper' and options[computer_choice]=='Rock'):
        winner_choice = 'Paper'
    elif (options[computer_choice] == 'Rock' and options[user_choice]=='Scissor') or (options[computer_choice]=='Scissor' and options[computer_choice]=='Rock'):
        winner_choice = 'Rock'
    else:
        winner_choice='Scissor'

if options[computer_choice]==winner_choice:
    print("The winner is The computer")
    print(computer_choice)
elif options[user_choice]==winner_choice:
    print("The winner is The user")
    print(computer_choice)




