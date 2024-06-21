"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Michal Vetr
email: michal.vetr@gmail.com
discord: michalvetr
"""

import re
from projekt_1_data import users
from projekt_1_data import TEXTS as texts

def separator():
    print("-" * 40)

def count_words(text:str):
    return len(text.split())

def count_title_cased_words(text:str) -> int:
    return len([word for word in text.split() if word.istitle()])

def count_uppper_cased_words(text:str) -> int:
    return len([word for word in text.split() if not word[0].isdigit() and word.isupper()])

def count_lower_cased_words(text:str) -> int:
    return len([word for word in text.split() if word.islower()])

def count_numeric_words(text:str) -> int:
    return len([word for word in text.split() if word.isdigit()])

def count_numeric_words_value(text:str) -> int:
    return sum([int(word) for word in text.split() if word.isdigit()])

def clean_text(text:str) -> str:
    return re.sub(r'[^A-Za-z0-9\s]', '', text)

def get_words_lengths(text:str) -> dict:
    word_count = {}
    for word in text.split():
      length = len(word)
      if length in word_count:
          word_count[length] += 1
      else:
          word_count[length] = 1

    # Sort the dictionary by keys (lenght of words)
    sorted_word_count = dict(sorted(word_count.items()))      
    return sorted_word_count

def display_word_lengths(word_count: dict):
    # Print the header
    print("----------------------------------------")
    print("LEN|  OCCURENCES  |NR.")
    print("----------------------------------------")
    
    # Print each length and its count
    for length, count in word_count.items():
        stars = '*' * count
        print(f"{length:>3}|{stars:<20}|{count}")    

def welcome(usr:str):
    separator()
    print(f"Welcome to the app, {usr}")
    print(f"We have 3 texts to be analyzed.")

def login(username:str, password:str) -> bool:
    if username in users:
        if users[username] == password:
            return True
    else:
        return False
    
# Ask for username and password
username = input("username:")
password = input("password:")

# Call login function
user_state=login(username, password)

if user_state:
    welcome(username)
    separator()
    text_choice = int(input("Enter a number btw. 1 and 3 to select:"))
    separator()

    text = (texts[text_choice-1])
    words=count_words(text)
    title_cased_words = count_title_cased_words(text)
    uppper_cased_words = count_uppper_cased_words(text)
    lower_cased_words = count_lower_cased_words(text)
    numeric_words = count_numeric_words(text)

    print(f"There are {words} in the selected text.")           # print(words)
    print(f"There are {title_cased_words} titlecase words.")    # print(title_cased_words)
    print(f"There are {uppper_cased_words} uppercase words.")   # print(uppper_cased_words)
    print(f"There are {lower_cased_words} lowercase words.")    # print(lower_cased_words)
    print(f"There are {numeric_words} numeric strings.")        # print(numeric_words)
    print(f"The sum of all the numbers {count_numeric_words_value(text)}") # print(f"The total number of numeric values is {count_numeric_words_value(text)}")

    text = clean_text(text)
    words_lengths = get_words_lengths(text)
    display_word_lengths(words_lengths)
    
else:
    print ("unregistred user, terminating the program..")



