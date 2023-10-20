import random as r
import string as str
import time as t

print("\n---------------------------------------- Welcome To The Password Generator ----------------------------------------\n\n" +

"Password length must be minimum 7 digit\n\n" +
         
"Letters = [a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z]\n\n" +
    
"Digits = [0 1 2 3 4 5 6 7 8 9]\n\nPunctuations = [ ! # $ % & ' ( ) * + , - . / : ; < = > ? @ [ ] ^ _ ` { | } ~ ]" +
        
"\n\nIf you want to quit please press the 'q' or 'Q'\n\n" +
    
"If you want to create password please press the 'y' or 'Y'\n\n"+
 "-------------------------------------------------------------------------------------------------------------------")

name = input("\nPlease write the your name: ")

button = input(f"\nDo you want to create a password {name.capitalize()}?\nAnswer: ")


while True:    
    
    if (button == 'q' or button == 'Q'):
        
        print(f"\nSee you then {name.capitalize()}\n")  
        
        break
        
    if (button == 'y' or button == 'Y'):
       
        password_length = int(input("\nPls enter the length of the password: "))
         
        if(password_length < 7):
        
            print("\nPassword length must be minimum 7 digit")
            
            print("Please read the description carefully !!!\n")
            
            password_length = int(input("\nPls enter the length of the password: "))
            
        repeat = int(input("\nHow many do you want password: "))
    
        print("\nPasswords are creating.\nThis process can take some time.\nPlease waiting...\n")
       
        t.sleep(5)
    
        for i in range(1,repeat+1):    
           
            chr = str.ascii_letters + str.digits + str.punctuation

            password = "".join(r.choice(chr) for x in range(0,password_length))

            print(f"Your {i}.password is {password}")
        
                 
    print("\nPlease don't share your passwords with anyone !!!!\n")

    print(f"See you then {name.capitalize()}\n")
    
    break