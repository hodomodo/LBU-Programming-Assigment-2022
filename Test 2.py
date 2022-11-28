# Imports the random module to randomise the selection from the list
import random

num_passwords = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# List off all words to be used as combinations in the passwords. There are 17 words giving 680 unique combinations and 969 combinations with repetitions
constants = ["abate", "arid", "compassion", "conditional", "digression", "diligent", "empathy", "florid", "foster",
             "frugal", "impute", "intrepid", "mundane", "orator", "parched", "manifesto", "tactful"]

# Welcomes the user to the program
print("Password Generator")
print("==================")

# Asks the user for the desired number of passwords
while True:
    no_passwords = input("How many passwords should be generated? (Minimum = 1, Maximum = 24) : ")
    # Attempts to convert the input into an integer
    try:
        no_passwords = int(no_passwords)
        if 1 <= no_passwords <= 24:
            # Loop breaks if the user input is valid
            break
        # If input is invalid the user will be asked for the input again and again
        else:
            print("Please enter a number between 1 and 24 (inclusive)")
    # If there is an error in converting, the user will be asked to try again
    except ValueError:
        print("Please input a number")

# Uses the users input to decide how many passwords to make.
for n in range(no_passwords):
    i = 0
    while i < len(num_passwords):
        # Password consists of a random (random.choices) combination of 3 (k=3) words from the list (constants)
        password = random.choices(constants, k=3)
        # Removes the [ and " and spaces from the items retrieved from the list
        print(num_passwords[i], "-->", "".join(password))
        i += 1
