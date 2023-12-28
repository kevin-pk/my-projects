import math 

# this program uses user input such as weight, height, to display the user bmi and bmi category 
# note to self (this program seems very straight forward, I should make this code a lot more interactive in terms of user input)

def start():
    greeting = input(""" hey there what's your name ? """)
    greeting1 = print(greeting), print( """ let's start""")
    explanation = input("""this is a bmi calculator, it is intended to help you find you BMI and tell you what catagories, 
    your score falls under.
    
    (enter ready to start.)""").title()
    
    while explanation != "Ready":
        print("please type ready to start")
        explanation = input()
    else:
        pass
    
    print(""" Body mass Index multiplies your weight and height and places you in the catagories (Normal weight,
    underweight, Overweight, and Obese. """)
    
    weight = int(input("enter you weight to start."))
    weight = weight/ 2.205
    feet = int(input("Ok so now input your height in feet.(example if you are 5 foot 8 inches you would put 5 in this colum) "))
    inches = int(input(" now you enter your height in inches, ( example if you were 5 foot 8 inches, you would enter 8 into the colum). "))
    height = (feet * 0.3048) + (inches * 0.0254)
    bmi = weight / (height ** 2)
    print(bmi)
    
    if bmi < 18.5:
        print("you are considered underweight.")
        
    elif bmi < 25:
        print(" you are considered to be Normal weight.")
    elif bmi < 29 :
        print("you are considered to be overweight. ")
    else:
        print("you are considered to be overweight.")
    










start()