from datetime import datetime

print(f"""\n----- Welcome To The Receipt Calculator -----
      
Time: {datetime.now()}\n""")

name = input("Please enter the name of company: ")

nameOfbuy = list()

number = int(input("\nHow many things did you buy?\nAnswer: "))

print()

for i in range(number):

    enter = input(f"{i+1}.product received: ")

    nameOfbuy.append(enter)

kdv_price_name = list()

print()

sum = 0

kdv = 0.18

for i in range(number):    

    buy = int(input(f"{i+1}.product price: "))     
     
    kdv_price =  buy * (kdv + 1)  
    
    kdv_price_name.append(kdv_price)
    
    sum += kdv_price

print(f"\nkdv = {kdv}")

print("\nProduct\t\tPrice\n-------\t\t-----")

for (i,j) in zip(nameOfbuy,kdv_price_name):     

    print(f"{i}\t\t{j}")      

result = 0

for i in range(len(kdv_price_name)):   
   
   result += kdv_price_name[i]   
  
print(f"\nTotal result is {result:.2f}") 
    
print()    