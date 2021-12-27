from random import randint

def take_turn(goal):
    guess = int(input("Please guess a number between 1 and 100: "))

    if guess < 1 or guess > 100:
        print("Hmm, you broke the rules! Please choose a number between 1 and 100.")
    else:
        if guess > goal:
            print("Sorry, your number is too high!")
        elif guess < goal:
            print("Sorry, your number is too low!")
        else:
            return True

    return False

def print_message(win):
    if win:
            print("Hooray! You got it right!")
    else:
        print("Oh, so sorry, you ran out of turns...")

def play_game():
    play_again = "Y"

    while play_again.lower() == "y":
        print("Guess a number in 5 turns!")

        did_you_win = False
        goal  = randint(1, 100)

        for turn in range(5):
            did_you_win = take_turn(goal)

        print_message(did_you_win)

        play_again = input("Would you like to play again (y/n): ")

    print("Thanks for playing my game!")

if __name__ == "__main__":
    play_game()