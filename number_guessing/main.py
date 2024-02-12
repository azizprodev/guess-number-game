from random import randint

def get_top_of_range():
    while True:
        top_of_range = input("Enter the top of the range => ")
        if top_of_range.lstrip("-").isdigit():
            top_of_range = int(top_of_range)
            if top_of_range <= 0:
                print("Please type a number greater than 0!")
            else:
                return top_of_range
        else:
            print("Please type a valid number!")

def get_guess():
    while True:
        guess_number = input("Guess a number => ")
        if guess_number.lstrip("-").isdigit():
            guess_number = int(guess_number)
            if guess_number < 0:
                print("Please type a number 0 or greater than 0!")
            else:
                return guess_number
        else:
            print("Please type a valid number!")

def play_game():
    top_of_range = get_top_of_range()
    random_number = randint(0, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        guess_number = get_guess()

        if guess_number == random_number:
            print("You got it!")
            break
        elif guess_number > random_number:
            print("Your guess is above the number!")
        else:
            print("Your guess is below the number!")

    print("You got it in", guesses, "guesses")

if __name__ == "__main__":
    play_game()
