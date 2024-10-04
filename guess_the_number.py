import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Randomly select a number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    # Game loop
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts}: What's your guess? "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
