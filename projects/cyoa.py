"""A choose your own adventure program that plays Rock, Paper, Scissors with the user."""

__author__ = "730312274"

from random import randint

ROCK: str = '\U0001F44A'
PAPER: str = '\U0000270B'
SCISSORS: str = '\U0000270C'
points: int = 0
player: str = ""
game_win: int = 0


def main() -> None:
    global points
    play_again: str = "Yes"
    greet()
    while play_again == "Yes":
        accepted_response: str = "No"
        if points > 0:
            points = multiplier(points)
        else:
            game()
        print(f"Good game, {player}! Your current score is {points}.")
        while accepted_response == "No":
            again: str = input("Would you like to play again? (yes/no) ")
            if again == "yes" or again == "Yes":
                play_again = "Yes"
                accepted_response = "Yes"
            elif again == "no" or again == "No":
                play_again = "No"
                accepted_response = "Yes"
            else:
                print("I'm not sure I understand. I'm looking for a 'yes' or 'no' response.")
    print(f"Thanks for playing! Your final score was {points}. Have a nice day!")


def greet() -> None:
    """To greet the player and ask for their name."""
    global player
    print("Hello! Today we are going to play Rock, Paper, Scissors.")
    player = input("What is your name? ")


def game() -> None:
    """The main game of Rock, Paper, Scissors."""
    global points
    global game_win
    game_action: str = ""
    accepted_response: str = "No"
    print(f"Let's play, {player}!")
    while accepted_response == "No":
        player_choice: str = input("Choose 'rock', 'paper', or 'scissors': ")
        if player_choice == "rock" or player_choice == "Rock" or player_choice == "paper" or player_choice == "Paper" or player_choice == "scissors" or player_choice == "Scissors":
            my_choice: int = int(randint(1, 3))
            accepted_response = "Yes"
            if my_choice == 1:
                game_action = "Rock " + ROCK
            elif my_choice == 2:
                game_action = "Paper " + PAPER
            elif my_choice == 3:
                game_action = "Scissors " + SCISSORS
            if my_choice == 1:
                if player_choice == "rock" or player_choice == "Rock":
                    print(f"I chose {game_action}! Looks like we tied.")
                    game_win = 1
                elif player_choice == "paper" or player_choice == "Paper":
                    print(f"I chose {game_action}! Looks like you won!")
                    points = points + 1
                    game_win = 2
                elif player_choice == "scissors" or player_choice == "Scissors":
                    print(f"I chose {game_action}! Looks I won.") 
                    game_win = 0
            elif my_choice == 2:
                if player_choice == "rock" or player_choice == "Rock":
                    print(f"I chose {game_action}! Looks like I won.")
                    game_win = 0
                elif player_choice == "paper" or player_choice == "Paper":
                    print(f"I chose {game_action}! Looks like we tied.")
                    game_win = 1
                elif player_choice == "scissors" or player_choice == "Scissors":
                    print(f"I chose {game_action}! Looks like you won!") 
                    points = points + 1
                    game_win = 2
            elif my_choice == 3:
                if player_choice == "rock" or player_choice == "Rock":
                    print(f"I chose {game_action}! Looks like you won!")
                    points = points + 1
                    game_win = 2
                elif player_choice == "paper" or player_choice == "Paper":
                    print(f"I chose {game_action}! Looks like I won.")
                    game_win = 0
                elif player_choice == "scissors" or player_choice == "Scissors":
                    print(f"I chose {game_action}! Looks like we tied.") 
                    game_win = 1
        else:
            print("I'm not sure I understand. I'm looking for a response of the word 'rock', the word 'paper', or the word 'scissors'.")


def multiplier(x: int) -> int:
    """Give the player the option to go double-or-nothing."""
    choice: str = ""
    accepted_input: str = "No"
    print("It looks like your score is greater than 0. If you're really confident you can beat me, you can go double-or-nothing.")
    print("If you choose to do so and win, I'll double your score rather than just adding 1 to it.")
    print("If you choose to do so and tie, your score won't be affected.")
    print("However, if you choose to do so and lose, I'll reset your score to 0!")

    while accepted_input == "No":
        choice = input("Would you like to go double-or-nothing? (yes/no) ")
        if choice == "yes" or choice == "Yes" or choice == "no" or choice == "No":
            accepted_input = "Yes"
            if choice == "yes" or choice == "Yes":
                game()
                if game_win == 2:
                    x = x * 2
                    print(f"Wow! Good job! I'll double your score to {x}!")
                elif game_win == 1:
                    x = points
                    print(f"Your score will be unaffected. It is {x}.")
                else:
                    x = 0
                    print(f"Oh-no! You score is now {x}!")
            else:
                game()
                x = points
        else:
            print("I'm not sure I understand. I'm looking for a 'yes' or 'no' response.")
    return x


if __name__ == "__main__":
    main()