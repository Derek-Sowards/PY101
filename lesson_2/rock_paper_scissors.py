import random
import os

#'Fighters' the user/computer can choose from
VALID_CHOICES = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors',
    'l': 'lizard',
    'sp': 'Spock',
}

#Clears the screen on a mac
def clear_screen():
    os.system('clear')

#Displays to the terminal, the rules of the game
def display_rules():
    prompt("""
    HERE ARE THE RULES:
           
    Scissors cuts Paper
    Paper covers Rock
    Rock crushes Lizard
    Lizard poisons Spock
    Spock smashes Scissors
    Scissors decapitates Lizard
    Lizard eats Paper
    Paper disproves Spock
    Spock vaporizes Rock
    Rock crushes Scissors
    ---------------------
           
       First to 3 wins!""")


#Function asking if the user would like to see the rules.
def welcome():
    prompt("""Welcome to rock, paper, scissors, lizard, spock,
        Would you like to view the rules (y/n)?""")
    answer = input().lower()
    while answer and answer[0] != "n" and answer[0] != "y":
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] != "n":
        display_rules()


#Asks the user if the program can continue forward
def ask_to_proceed():
    while True:
        print("""\nAre you ready to continue (y/n)?""")
        choice = input().strip().lower()
        while choice[0] != "n" and choice[0] != "y":
            prompt('Please enter "y" or "n".')
            choice = input().lower()
        if choice[0] != "n":
            clear_screen()
            break
        prompt('okay, lets wait here...')


#Makes printing messages have an arrow
def prompt(message):
    print(f"==> {message}")


#Returns a string of the winner: 'player'/'computer'/'tie'
def find_winner(player, computer):
    winning_combos = {
        'r':     ['s', 'l'],
        'p':     ['r', 'sp'],
        's':     ['p', 'l'],
        'l':     ['p', 'sp'],
        'sp':    ['r', 's'],
}
    if computer in winning_combos[player]:
        return 'player'
    if player == computer:
        return 'tie'
    return 'computer'

#Displays winner from the string
def display_winner(winner_string, player_choice, computer_choice):
    prompt(f"""You chose {VALID_CHOICES[player_choice]},
    Computer chose {VALID_CHOICES[computer_choice]}""")
    match winner_string:
        case 'player':
            prompt('You win!')
        case 'computer':
            prompt('Computer wins!')
        case 'tie':
            prompt("It's a tie!")

#Gets players choice of fighter
def get_player_choice():
    prompt("""Choose your fighter by typing the corresponding character(s):
    'r' for rock
    'p' for paper
    's' for scissors
    'l' for lizard
    'sp' for Spock""")
    choice = input().strip().lower()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input().strip().lower()
    return choice

#Gets computers choice of fighter
def get_computer_choice():
    return random.choice(list((VALID_CHOICES.keys())))

#Updates the scoreboard
# def update_scoreboard(winner_string):
#     if winner_string == 'player':
#         scoreboard[winner] += 1
#     elif winner_string == 'computer':
#         scoreboard[winner] += 1
#     else:
#         pass
def update_scoreboard(winner_string, scoreboard):
    if winner_string in ('player', 'computer'):
        scoreboard[winner_string] += 1

#Displays scoreboard
def display_scoreboard(scoreboard):
    print(f"""
         ---SCOREBOARD---
    {scoreboard}
""")




#function that contains the logic of gameplay
def play():
    while True:

        scoreboard = {'player': 0, 'computer': 0}
        welcome()
        ask_to_proceed()

        while scoreboard['player'] < 3 or scoreboard['computer'] < 3:

            player_choice = get_player_choice()
            computer_choice = get_computer_choice()
            clear_screen()

            winner = find_winner(player_choice, computer_choice)
            display_winner(winner, player_choice, computer_choice)

            update_scoreboard(winner, scoreboard)
            display_scoreboard(scoreboard)

            if scoreboard['player'] < 3 and scoreboard['computer'] < 3:
                ask_to_proceed()

            if scoreboard['player'] == 3:
                prompt('Congrats! You are the champion!')
                break
            if scoreboard['computer'] == 3:
                prompt('Better luck next time!')
                break


        #Breaks out of loop and asks user if they would like to play again
        while True:
            play_again = input('Would you like to play again (y/n)?\n'
                            ).lower().strip()
            if play_again in {'y', 'n'}:
                break
            prompt('Please enter "y" or "n".')

        if play_again == 'n':
            prompt("Thanks for playing!")
            break

#Call the play function to start the game
play()