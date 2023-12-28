# 
# the goal of this project is to have a computer generated random password
# the user should be able to change the ingredients of the password such as special characters, does the password have number ? etc
# this project draws similarities to a password generator found on smartphones today, that allow for the 


import random 
import string 

def make_password(min_length , numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
        
    pwd= ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True
            
            meets_criteria = True
            if numbers:
                meets_criteria = has_number
            if special_characters:
                meets_criteria = meets_criteria and has_special
                
    return pwd

min_length = int(input("enter the length of the password "))
has_number = input("should the password have numbers in it (y/n) ").lower()== "y"
has_special = input("Should the password have special characters ? (y/n) ").lower() == 'y'

pwd = make_password(min_length,has_number,has_special) 
print("the password generated is:" , pwd)