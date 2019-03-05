# 4. Rock, paper, scissors game - Bot v hooman

import random as rand

options = range(1,4)


def bot_weapon_choice():
    return rand.choice(options)


def selected_weapon(weapon: int):
    if weapon == 1:
        return "weapon of choice is DA PAPER"
    elif weapon == 2:
        return "weapon of choice is DA ROCK"
    elif weapon == 3:
        return "weapon of choice is DA SCISSORS"


def select_winner(bot_weapon: int, losing_bot_weapon: int):
    if bot_weapon == losing_bot_weapon:
        print("You won!")
    else:
        print("The bot won :(")


def fight(player_weapon: int, bot_weapon: int):
    print(f'Your {selected_weapon(player_weapon)}')
    print(f"The bot's selected {selected_weapon(bot_weapon)}")
    if player_weapon == 1:
        select_winner(bot_weapon=bot_weapon, losing_bot_weapon=2)
    elif player_weapon == 2:
        select_winner(bot_weapon=bot_weapon, losing_bot_weapon=3)
    elif player_weapon == 3:
        select_winner(bot_weapon=bot_weapon, losing_bot_weapon=1)


def play_again():
    while True:
        user_input = input('Would you like to play again? (y/n) ')
        if user_input == 'y':
            user_weapon()
        elif user_input == 'n':
            print('Exiting...')
            exit()
        else:
            print("That's not an option my dude. Please type y or n :)")


def user_weapon():
    print(
        "Welcome to the annual clash of paper, rock, scissors! Today you will be fighting" +
        " against the most formidable bots. Ready your horses and let's begin!"
    )
    while True:
        print('Select your weapon:')
        user_input = input('(1)Paper (2)Rock (3)Scissors')
        if user_input.isdigit():
            fight(player_weapon=int(user_input), bot_weapon=bot_weapon_choice())
            play_again()
        else:
            print("That's not an option my dude. Please select 1, 2 or 3.")


user_weapon()
