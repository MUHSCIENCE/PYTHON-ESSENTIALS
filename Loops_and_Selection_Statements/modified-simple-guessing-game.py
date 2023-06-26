import random
import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

# Calculate the minimum number of guesses needed
min_guesses = math.ceil(math.log(larger - smaller + 1, 2))

print("Think of a number between", smaller, "and", larger)
print("You can give 'L' if the guess is too low, 'H' if it's too high, or 'C' if it's correct.")

count = 0
low = smaller
high = larger

while True:
    count += 1
    guess = random.randint(low, high)
    response = input("Is it " + str(guess) + "? (L / H / C): ")

    if response.upper() == 'L':
        low = guess + 1
    elif response.upper() == 'H':
        high = guess - 1
    elif response.upper() == 'C':
        print("Congratulations! The computer guessed it in", count, "tries!")
        break
    else:
        print("Invalid response. Please enter 'L', 'H', or 'C'.")

    if count >= min_guesses:
        print("Oops! The computer couldn't guess your number in the minimum number of tries.")
        print("Make sure you didn't give any misleading hints.")
        break
