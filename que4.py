# Write python function name 'number_gussing_game' that allows the user to guess ramdamly ganreted number between 1 and 100. the user has 9 trailas to guss the number. after each guss the function should return :
#  * "congractulations! you gussed it right!" if the guess is correct.
#  * "Too low! try again" if the guess is less then the target number.
#  "Too high! try again " if the guess greater then the target number. if user fails the guess the number within 9 trails, return "sorry tou have used all your trails. the number was [number].

'''import random

def number_guessing_game():
    # Generate random number from 1 to 100
    random_number = random.randint(1, 100)
    # Number of trials
    max_trials = 9
    # Loop for number of trials
    for trial in range(max_trials):
        # Prompt the user to enter a guess
        try:
            guess = int(input("Enter your number (1-100): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        # Check the guess against the target number 
        if guess == random_number:
            print("Congratulations! You guessed it right!")
            return
        elif guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    
    # If the loop finishes without a correct guess
    print(f"Sorry, you have used all your trials. The number was {random_number}.")

# To run the game, simply call the function
number_guessing_game()'''





'''import random
def number_gussing_game():
    gusses_number= random.randint(0,100)
    print(gusses_number)
    max_trail = 9
    count = 0
    for trail in range (max_trail):
        number =int(input("Enter a number"))
        if trail < max_trail:
            print("sorry you have only 9 trail")
        else:
            print("sorry you have use all trail")
    while True:
        #number = int(input("Enter a number"))
        if number == gusses_number:
            print("congretions! number is right")
            break
        elif number < gusses_number:
            print("Too low! try again")
        else :
            print("Too high! try again")
number_gussing_game()'''

# Write python function name 'number_gussing_game' that allows the user to guess ramdamly ganreted number between 1 and 100. the user has 9 trailas to guss the number. after each guess the function should return :
#  * "congractulations! you gussed it right!" if the guess is correct.
#  * "Too low! try again" if the guess is less then the target number.
#  "Too high! try again " if the guess greater then the target number. if user fails the guess the number within 9 trails, return "sorry tou have used all your trails. the number was [number].

import random

def number_guessing_game():
    guessed_number = random.randint(0, 100)  # Random number between 0 and 100
    print(guessed_number)
    max_trials = 9  # Max number of attempts
    #print("You have 9 attempts to guess the number between 0 and 100.")
    
    for trial in range(1, max_trials + 1):
        number = int(input("Entar a number: " ))
        
        if number == guessed_number:
            print(f"Congratulations! You guessed the number {guessed_number} correctly in {trial} attempts!")
            break
        elif number < guessed_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        
        if trial == max_trials:
            print(f"Sorry, you've used all {max_trials} attempts. The correct number was {guessed_number}.")
        
number_guessing_game()


