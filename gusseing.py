import random

# Get range from user
range_num = int(input("Enter a number for the range: "))

# Generate random number
secret_num = random.randint(1, range_num)

# Initialize guess count
guess_count = 0

# Keep looping until user guesses the correct number
while True:
    # Get guess from user
    guess = int(input("Guess a number between 1 and {}: ".format(range_num)))
    
    # Increase guess count
    guess_count += 1
    
    # Check if guess is correct
    if guess == secret_num:
        print("Congratulations! You guessed the number in {} guesses.".format(guess_count))
        break
    elif guess < secret_num:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

        