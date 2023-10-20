import random as r 
import time as t 

print("\n---------- Welcome To The Guessing Number Game ---------\n\nIf you want to quit please press the 'q' or 'Q'\n\n"+
    
"If you want to play the game please press the 'y' or 'Y'\n\n--------------------------------------------------------\n\n")

counter = 1
    
name = input("Please write your name: ")

surname = input("Please write your surname: ")

user = input(f"\nAre you ready for the game {name.capitalize()}?\nAnswer: ")


if(user == 'q' or user == 'Q'): 
     
    print(f"See you then {name.capitalize()}\t{surname.upper()}")
    
    exit() 
 
   
guess_right = int(input("\nHow many do you want guess rigth: "))

bottom = int(input("\nPlease enter the bottom number: "))  
    
top = int(input("\nPlease enter the top number: "))
    
print(f"Guess number between [{bottom}-{top}]")
        
print(f"\nGood Luck :)\n{name.capitalize()}\t{surname.upper()}")

random_number = r.randrange(bottom,top)

    
while (user == "y" or user == "Y"):
    
    guess_number = int(input("\nPlease enter the guess: "))
                            
    print("\nYour prediction is being analysed")
    
    t.sleep(2) 
     
    if(guess_number > random_number):
        
        print(f"\nToo High!\nYour guess was too high.\nTry again!")
        
        guess_right -= 1
                
        counter += 1
            
    elif(guess_number < random_number):
        
        print(f"\nToo Low\nYour guess was to low.\nTry again!")    
        
        guess_right -= 1
            
        counter += 1               
    
    else:
        
        print(f"Congratulations, you got the number right in {counter} guesses.")
        
        again = input("\nDo you want to play again ?\nAnswer: ")
        
        if(again == "y" or again == "Y"):
            
            guess_right = int(input("\nHow many do you want guess rigth: "))

            bottom = int(input("\nPlease enter the bottom number: "))  
    
            top = int(input("\nPlease enter the top number: "))
    
            print(f"Guess number between [{bottom}-{top}]")
        
            print(f"\nGood Luck :)\n{name.capitalize()}\t{surname.upper()}")

            random_number = r.randrange(bottom,top)

            continue
        
        elif(again == "q" or again == "Q"):
            
            print(f"See you then {name.capitalize()}\t{surname.upper()}")
            
            break 
    
    if(guess_right == 0):
        
        print(f"\nGame Over !!!\nYou didn't guess the number\nThe number is {random_number}")   
        
        again = input("\nDo you want to play again ?\nAnswer: ")
        
        if(again == "y" or again == "Y"):
            
            guess_right = int(input("\nHow many do you want guess rigth: "))

            bottom = int(input("\nPlease enter the bottom number: "))  
    
            top = int(input("\nPlease enter the top number: "))
    
            print(f"Guess number between [{bottom}-{top}]")
        
            print(f"\nGood Luck :)\n{name.capitalize()}\t{surname.upper()}")

            random_number = r.randrange(bottom,top)

            continue
        
        elif(again == "q" or again == "Q"):
            
            print(f"See you then {name.capitalize()}\t{surname.upper()}")
            
            break