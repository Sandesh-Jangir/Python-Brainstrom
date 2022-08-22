import random

# Generating the number
generated_number = random.randint(1, 100)

# (important) For Debugging Purposes only  
# print(generated_number)

# The Logic
guessed = False
guesses_took = 0
while guessed==False:
    guesses_took += 1
    number = int(input("Guess: "))
    if number == generated_number:
        print("congrats!!")
        print(f"Score: {100-guesses_took}")
        guessed = True
    elif number < generated_number:
        print("Higher")
    else:
        print("Lower")