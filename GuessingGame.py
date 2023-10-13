#Michael Dupuis_CIS261_GuessingGame
import random

def display_heading():
    print("Guess the number!")


def start_game(limit):
    number = random.randint(1, limit)
    print(f"Guess the number between 1 and {limit}\n.")
    count = 1
    guess = int(input("Your guess?: "))
    
    while(guess != number):
        if guess < number:
            print("Guess again, your number is too low")
            count += 1
        elif guess > number:
            print("Guess again, your number is too high")
            count += 1
        guess = int(input("What is your new guess?: "))
    print(f"You guessed it in {count} tries. \n")
    print()
    
def main():
    display_heading()
    again = "yes"
    while again.lower() == "yes":
        limit = int(input("Enter the limit: "))
        start_game(limit)
        again = input("would you like to play again? Enter (yes/no): ")
        print()
    print("Thanks for playing!")
    

if __name__ == "__main__":
    main()

   