import random

def roll_dice():

    """Rolls a six-sided dice and returns the result."""

    return random.randint(1, 6)

def play_game():

    """Plays a game between two players."""

    print("\nWelcome to the Dice Game!")
    print("The objective of the game is to be the first player to reach a total score of 10 or more.")
    print("Each player takes turns rolling a six-sided dice.")
    print("The number rolled is added to the player's total score.")
    print("The game will randomly decide who starts first.\n")

    # Get players' names
    player1_name = input("\nEnter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    # Randomly select the starting player
    starting_player = random.choice([1, 2])
    print(f"\n{['', player1_name, player2_name][starting_player]} starts the game!")

    # Initialize scores and set current player
    player1_score = 0
    player2_score = 0
    current_player = starting_player

    # Main game loop
    while player1_score < 10 and player2_score < 10:
        input("\nPress Enter to roll the dice...")
        dice_roll = roll_dice()
        print(f"{['', player1_name, player2_name][current_player]}'s turn: {dice_roll}")
        
        # Update the current player's score and print it
        if current_player == 1:
            player1_score += dice_roll
            print(f"{player1_name}'s total score: {player1_score}")
            if player1_score >= 10:
                print(f"\n{player1_name} wins!\n")
                break
            current_player = 2
        else:
            player2_score += dice_roll
            print(f"{player2_name}'s total score: {player2_score}")
            if player2_score >= 10:
                print(f"\n{player2_name} wins!\n")
                break
            current_player = 1
    
    # Ask if players want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        answer=input("\nReally ?! (y/n) : ")
        if answer.lower() =="n":
            print("\nsoo, we can startt :dd \n ")
            play_game()

        else:
            print("\nokey, chaoo\n")


def main():

    """Main function to start the game."""

    play_game()

if __name__ == "__main__":
    main()
