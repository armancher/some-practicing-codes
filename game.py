import random

WORDS = ("python", "java", "ruby", "javascript", "html", "css", "php", "swift")

word = random.choice(WORDS)
correct = word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("Welcome to the Word Jumble Game!")
print("Unscramble the letters to make a word.")
print("The jumbled word is:", jumble)

guess = input("Enter your guess: ")
guess = guess.lower()

while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Enter your guess: ")
    guess = guess.lower()

if guess == correct:
    print("Congratulations, you guessed it!")
