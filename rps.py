"""
The name of this game is Rock, Paper, Scissors. This version includes a replay option.
The user is asked to select either Rock, Paper, or Scissors.
The computer then randomly selects either Rock, Paper, or Scissors.
The user’s choice is compared to the computer’s choice and the winner is determined.
"""

# we need the randint function since the computer will select Rock, Paper, Scissors randomly
from random import randint
 
print('''
Welcome to Rock, Paper, Scissors!
Make your selection. Then the computer randomly makes a selection.
Both selections are compared to determine the winner.
Rock beats scissors; scissors beat paper; paper beats rock.
''')


options = ["ROCK", "PAPER", "SCISSORS"]

# the program will need to print win/lose messages to the user later
message = {"tie":"It's a tie!", "won":"Congratulations, you won!", "lost":"Sorry, you lost!"}

# we need a function that will decide the winner
def decide_winner(user_choice, computer_choice):
  print("You selected: %s" % user_choice)
  print("Computer selected: %s" % computer_choice)

  # this is how we determine the result
  if user_choice == computer_choice:
    print(message["tie"])
  # consider other scenarios where the user could win
  elif user_choice == options[0] and computer_choice == options[2]:
    print(message["won"])
  elif user_choice == options[1] and computer_choice == options[0]:
    print(message["won"])
  elif user_choice == options[2] and computer_choice == options[1]:
    print(message["won"])
  # user lost if it is not a tie and user did not win
  else:
    print(message["lost"])

# now we need a function that actually starts the game
def play_RPS():
  # prompt the user for their selection
  user_choice = input("Enter Rock, Paper, or Scissors: ")
  # convert the user's choice to uppercase in case she types in lowercase
  user_choice = user_choice.upper()
  # the computer's choice has to be random
  computer_choice = options[randint(0,2)]

  # the selections are all in and now it is time to determine a winner
  decide_winner(user_choice, computer_choice)
  

# While loop to keep running the game 
while True:
    
    play_game = input('Are you ready to play? Enter Y or N.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False


    # Game play
    while game_on:
        
        # call function that starts game
        play_RPS()

        # this version includes a replay option
        replay = input('Do you want to play again? Enter Y or N: ')
    
        if replay.lower()[0] == 'y':
            replay = True
        else:
            print("Goodbye.")
            replay = False
            break
    # break out of the while loop on replay
    break
    