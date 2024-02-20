
'''
projekt_2.py: second project to Engeto Online Python Akademie

author: Markéta Giňovská
email: marketa.ginovska@gmail.com
discord: MarketaGi
'''



import random
import time
import json
import os


# file name for statistics
#file_name = r"C:\Users\marke\PythonEngeto\Project_2\statistics.txt"
file_name = r".\statistics.txt"

# Check if the file exists, if not, create it
if not os.path.exists(file_name):
    with open(file_name, 'w'):
        pass  # This will create an empty file

def generate_secret_number():
    """Generates a secret 4-digit number with unique digits."""
    while True:
        digits = random.sample(range(10), 4)  # číslice 1-9 (nesmí začínat 0)
        if digits[0] != 0:
        #random.shuffle(digits)
            secret_number = ''.join(map(str, digits[:4]))  # Creating secret number
        return secret_number

def has_duplicates(input_str):
    """Checks if the input string contains duplicate digits."""
    return len(set(input_str)) != len(input_str)
    
def play_game():
    """Hra Bulls and Cows.
       Generates a random 4-digit number for the player to guess. The player 
       repeatedly enters guesses until they correctly guess the number.  
    
    """
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

    secret_number = generate_secret_number()
    #print(secret_number)
    guesses = 0
    previous_guesses = set()
    bulls = 0
    cows = 0
    start_time = time.time()

    while True:
        user_input = input("Enter a number: ")

        if len(user_input) != 4: 
            print("Your input is longer or shorter than 4 characters.")
        elif user_input[0] == '0':
            print("Your input starts with 0 and this is not allowed.")
        elif not user_input.isdigit():
            print("Your input contains non-numeric values.")
        elif user_input in previous_guesses:
            print("You have already guessed this number. Try a different one.")
        elif has_duplicates(user_input):
            print("Your input contains duplicate digits.")
        elif user_input == secret_number:
            #elapsed time till we know the result
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Correct, you've guessed the right number in {guesses + 1} guesses in {elapsed_time:.2f} seconds!")

            #result of guesses count to statistics.txt 
            game_result = guesses + 1
            with open(file_name, 'r') as file:
                file_content = file.read().strip()

            # if file is empty, we cannot count average
            if not file_content:
                print("File does not contain any data.")
            else:
                # Splitting the content of the file by new lines and converting it into a list of numbers.
                print(file_content)
                numbers = [int(val) for val in file_content.split('\n')]
    
                # Calculation of the average values.
                average = sum(numbers) / len(numbers)
    
                #print(f"The average value in the file is: {average}")

                if game_result > average:
                    print("You are worse then average...")
                elif game_result == average:
                    print("You have achieved average result!")
                elif game_result < average:
                    print("Amazing! You are better then average!")

            with open(file_name, 'a') as file:
                file.write(str(game_result) + "\n")
            break

        else:
            previous_guesses.add(user_input)
            guesses += 1
            bulls = 0
            cows = 0

            for i in range(4): 
                if user_input[i] == secret_number[i]:  
                    bulls += 1
                    
                elif user_input[i] in secret_number: 
                    cows += 1

            print(f"Bulls: {bulls} {'bull' if bulls == 1 else 'bulls'}")
            print(f"Cows: {cows} {'cow' if cows == 1 else 'cows'}")


# run the game
play_game()

