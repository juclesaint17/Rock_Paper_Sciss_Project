import random
from webbrowser import get


def get_computer_choice():
    
    #create a list to store choices
    choice_list = ['Rock','paper','scissors']

    # select the choice randomly from the choice_list
    computer_choice = random.choice(choice_list)

    return computer_choice


def get_user_choice():
    # ask for user input. the user select one input
    choice = input('select input /rock/papers/scissors: ')
    return choice

def get_winner(computer_choice, user_choice):

    if computer_choice != user_choice:
        print('The computer choice is {}, and your choice is {}. The computer wins'.format(computer_choice,user_choice))
    elif computer_choice == user_choice:
        print('The computer choice is {}, and your choice is {}. You wins'.format(computer_choice,user_choice))
    else:
        print('reload the game')

def play():
    system_choice = get_computer_choice()
    player = get_user_choice()
    get_winner(system_choice,player)

play()

