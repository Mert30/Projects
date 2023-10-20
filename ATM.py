import time as t 

print("\n--------------- Welcome To The ATM ---------------\n\nOperations:\n\n1)Withdraw Money\n2)Adding Money\n3)Balance Inquiry\n4)Continue to operate\n"+
      "5)Exit from the ATM\n" + "---------------------------------------------------------\n")

name = input("Please write your name: ") 

budget = int(input(f"\nHow much money is in your account {name.capitalize()}?\nBudget: $")) 


while True:

    user_choice = input("\nPlease select the operation: ")  

    if(user_choice == "5"):
       
       print(f"\nExiting the ATM...\nPlease waiting...")
       
       t.sleep(2)
       
       print(f"\nGood Day {name.capitalize()}")
       
       break
     
    if(user_choice == "1"):
   
        amount = int(input("\nPlease enter the amount of money to be withdrawn: $"))
        
        if(amount > budget):
            
            print(f"\nWARNING : You don't have that much money in your account to withdraw!!!\n\nYou have ${budget} in your account")
            
            amount = int(input("\nPlease enter the amount of money to be withdrawn: $"))
            
            budget -= amount
             
            print("\nYour money is being withdrawn from your account.\nPlease waiting...")
    
            t.sleep(2)
       
            print(f"\nThe amount remaining in your account is ${budget}")

            answer = input("\nWill you continue to operate ?\nAnswer:")
        
            if(answer == "4"):
            
                continue
        
            elif(answer == "5"):
        
                print(f"\nExiting the ATM...\nPlease waiting...")
       
                t.sleep(2)
       
                print(f"\nGood Day {name.capitalize()}\n")
       
                break
        else:     
            
            budget -= amount
   
            print("\nYour money is being withdrawn from your account.\nPlease waiting...")
    
            t.sleep(2)
       
            print(f"\nThe amount remaining in your account is ${budget}")

            answer = input("\nWill you continue to operate ?\nAnswer:")
        
            if(answer == "4"):
            
                continue
        
            elif(answer == "5"):
        
                print(f"\nExiting the ATM...\nPlease waiting...")
       
                t.sleep(2)
       
                print(f"\nGood Day {name.capitalize()}\n")
       
                break
        
               
    elif(user_choice == "2"):    

        amount = int(input("\nPlease enter the amount to be added to your account: $"))
   
        budget += amount
   
        print("\nYour money is being added to your account.\nPlease waiting...")
    
        t.sleep(2)
       
        print(f"\nYour budget is ${budget}") 
        
        answer = input("\nWill you continue to operate ?\nAnswer:")
        
        if(answer == "4"):
            
            continue
        
        elif(answer == "5"):
            
            print(f"\nExiting the ATM...\nPlease waiting...")
       
            t.sleep(2)
       
            print(f"\nGood Day {name.capitalize()}\n")
       
            break

    elif(user_choice == "3"):
    
        print("\nThe money in your account will be shown in a moment.\nPlease waiting...")
    
        t.sleep(2)
       
        print(f"\nYour budget is ${budget}")
        
        answer = input("\nWill you continue to operate ?\nAnswer:")
        
        if(answer == "4"):
            
            continue
        
        elif(answer == "5"):
            
            print(f"\nExiting the ATM...\nPlease waiting...")
       
            t.sleep(2)
       
            print(f"\nGood Day {name.capitalize()}\n")
       
            break
        
    elif(user_choice != range(1,5)):
        
        print("\nPlease enter a valid operation!!!") 
        
        continue   