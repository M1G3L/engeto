"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Michal Vetr
email: michal.vetr@gmail.com
discord: michalvetr
"""

import time
from functions import welcome, separator, get_random_int, display_bulls_cows, get_user_input, evaluate_performance, find_bulls_and_cows


# main function
if __name__ == "__main__":
    
    print(welcome())
    random_number = get_random_int()
    input_number = 0
    guess_count = 0

    print("Enter a number:")
    print(separator())

    start_time = time.time()
    while input_number != random_number:
        
        input_number = get_user_input()
        
        #result = bull_or_cow(random_number, input_number)
        result = find_bulls_and_cows(random_number, input_number)
        # get the result from dictionary
        
        if result["bulls"] != 4:
            print(display_bulls_cows(result["bulls"], result["cows"]))
            print(separator())
        guess_count += 1
    
    else:
        stop_time = time.time()
        print("Correct, you've guessed the right number")
        print(f"In {guess_count} guesses.")
        print(separator())
        print(evaluate_performance(guess_count))
        print(f"And it take you: {stop_time - start_time:.2f} seconds")

    
