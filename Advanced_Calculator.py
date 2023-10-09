import math 
import time as t

class Calculator:

    def start(self):
        self.Menu()
        choice = self.Choice()
        print(f"You have selected operation {choice}")
        
        if(choice == 1): self.Quit() 
        if(choice == 2): self.Owner()  
        if(choice == 3): self.Add() 
        if(choice == 4): self.Subraction() 
        if(choice == 5): self.Multiplication()  
        if(choice == 6): self.Divided()
        if(choice == 7): self.Sin()
        if(choice == 8): self.Cos()
        if(choice == 9): self.Tan()
        if(choice == 10): self.Cot()
        if(choice == 11): self.Sec()
        if(choice == 12): self.Cosec()
        if(choice == 13): self.Sqrt()
        if(choice == 14): self.Exp()
        if(choice == 15): self.Radians_To_Degrees()
        if(choice == 16): self.Degree_To_Radian()
        if(choice == 17): self.Abs()
        if(choice == 18): self.Mod()
        if(choice == 19): self.Log()
        if(choice == 20): self.Exponent()
        if(choice == 21): self.Ceil()
        if(choice == 22): self.Floor()
        if(choice == 23): self.Factoriel()
        if(choice == 24): self.Log10()
        if(choice == 25): self.Log2()
        
        
    def Choice(self):
        while True:
           try: 
              choice = int(input("Pls select the choice : "))
              while(choice < 1 or choice > 23):
                  choice = int(input("Pls enter the number between 1 to 23 : "))
              break  
           except ValueError:
               print("Pls enter the number!!")
        return choice
    
    def Menu(self):
       print("""\n******* Welcome To The Calculator *******\n\n---Operations On The Calculator---\n[1] Quit\n[2] Owner\n[3] Add\n[4] Subtraction\n[5] Multiplication\n[6] Divided\n[7] Sin
[8] Cos\n[9] Tan\n[10] Cot\n[11] Sec\n[12] Cosec\n[13] SquareRoot\n[14] Explonation\n[15] Conversion from radians to degrees\n[16] Conversion from degrees to radians
[17] Absolute Value\n[18] Mod\n[19] Log\n[20] Exponent\n[21] Ceil\n[22] Floor\n[23] Factoriel\n[24] Log10\n[25] Log2""")  
       t.sleep(1) 
        
    def Add(self):
        while True:
           try: 
              num1 = int(input("Pls enter the number 1 : "))
              num2 = int(input("Pls enter the number 2 : "))
              break
           except ValueError:
               print("Pls enter the number!!") 
        result = num1 + num2
        print("Pls wait the result !!!")
        t.sleep(1)
        print(f"{num1} + {num2} = ",result)
        return result
          
    def Subraction(self): 
        while True:
           try: 
              num1 = int(input("Pls enter the number 1 : "))
              num2 = int(input("Pls enter the number 2 : "))
              break
           except ValueError:
               print("Pls enter the number!!") 
        result = num1 - num2
        print("Pls wait the result !!!")
        t.sleep(1)
        print(f"{num1} - {num2} = ",result)    
        return result
    
    def Multiplication(self):
        while True:
           try: 
              num1 = int(input("Pls enter the number 1 : "))
              num2 = int(input("Pls enter the number 2 : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = num1 * num2
        print("Pls wait the result !!!")
        t.sleep(1)
        print(f"{num1} * {num2} = ",result)
        return result
    
    def Divided(self):
        while True:
           try: 
              divided = int(input("Pls enter the divided : "))
              divider = int(input("Pls enter the divider : "))              
              break
           except ValueError:
               print("Pls enter the number!!")
           except ZeroDivisionError:
               print("Pls dont divided by 0")
        result = (float)(divided/divider)
        print("Pls wait the result !!!")  
        t.sleep(1)        
        print(f"{divided} / {divider} = ",result)
        return result
    
    def Sin(self): 
        while True:
           try: 
              num = int(input("Pls enter the number : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = math.sin(math.radians(num))  
        print("Pls wait the result !!!") 
        t.sleep(1)   
        print(f"sin({num}) = ",result)
        return result
        
    def Cos(self):
        while True:
           try: 
              num = int(input("Pls enter the number : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = math.cos(math.radians(num)) 
        print("Pls wait the result !!!")    
        t.sleep(1)  
        print(f"cos({num}) = ",result)
        return result
    
    def Tan(self): 
        while True:
           try: 
              num = int(input("Pls enter the number : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = math.tan(math.radians(num))  
        print("Pls wait the result !!!")    
        t.sleep(1) 
        print(f"tan({num}) = ",result)
        return result

    def Cot(self):
        while True:
           try: 
              num = int(input("Pls enter the number : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = (float)(math.cos(math.radians(num)) / math.sin(math.radians(num))) 
        print("Pls wait the result !!!")    
        t.sleep(1)  
        print(f"cot({num}) = ",result)
        return result
    
    def Sec(self):
        while True:
           try: 
              num = int(input("Pls enter the number : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = (float)(1 / math.cos(num))  
        print("Pls wait the result !!!")  
        t.sleep(1)   
        print(f"sec({num}) = ",result)
        return result
     
    def Cosec(self):
        while True:
           try: 
              num = int(input("Pls enter the number : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = (float)(1 / math.sin(math.radians(num))) 
        print("Pls wait the result !!!")  
        t.sleep(1)    
        print(f"cosec({num}) = ",result)
        return result
     
    def Exponent(self):
        while True:
           try: 
              base = int(input("Pls enter the base : "))
              exponent = int(input("Pls enter the exponent : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = math.pow(base,exponent)       
        print("Pls wait the result !!!")
        t.sleep(1)
        print(f"pow({base},{exponent}) = ",result)
        return result
    
    def Ceil(self): 
        while True:
           try: 
              num = int(input("Pls enter the number : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = math.ceil(num)       
        print("Pls wait the result !!!")
        t.sleep(1)
        print(f"ceil({num}) = ",result)
        return result
    
    def Floor(self): 
        while True:
           try: 
              num = int(input("Pls enter the number : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = math.floor(num)       
        print("Pls wait the result !!!")
        t.sleep(1)
        print(f"floor({num}) = ",result)
        return result
    
    def Sqrt(self):
        while True:
           try: 
              num = int(input("Pls enter the number : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = math.sqrt(num)       
        print("Pls wait the result !!!")
        t.sleep(1)
        print(f"sqrt({num}) = ",result)
        return result
     
    def Exp(self):
        while True:
           try: 
              num = int(input("Pls enter the number : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = math.exp(num)     
        print("Pls wait the result !!!") 
        t.sleep(1) 
        print(f"exp({num}) = ",result)
        return result
    
    def Log(self):
        while True:
           try: 
              num = int(input("Pls enter the number : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = math.log(num)
        print("Pls wait the result !!!")   
        t.sleep(1)    
        print(f"log({num}) = ",result)
        return result
    
    def Log10(self):
        while True:
           try: 
              num = int(input("Pls enter the number : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = math.log10(num)
        print("Pls wait the result !!!")   
        t.sleep(1)    
        print(f"log10({num}) = ",result)
        return result
    
    def Log2(self):
        while True:
           try: 
              num = int(input("Pls enter the number : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = math.log2(num)
        print("Pls wait the result !!!")   
        t.sleep(1)    
        print(f"log2({num}) = ",result)
        return result
    
    def Factoriel(self):
        while True:
           try: 
              num = int(input("Pls enter the number : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        result = math.factorial(num)  
        print("Pls wait the result !!!")
        t.sleep(1)     
        print(f"Factoriel({num}) = ",result)
        return result
         
    def Mod(self):
        while True:
           try: 
              divided = int(input("Pls enter the divided : "))
              divider = int(input("Pls enter the divider : "))
              break
           except ValueError:
               print("Pls enter the number!!")
        remain = divided % divider  
        print("Pls wait the result !!!")   
        t.sleep(1)  
        print(f"Mod({divided},{divider}) = ",remain)
        return remain
            
    def Degree_To_Radian(self):
        while True:
           try: 
               degrees = float(input("Enter the degrees: "))
               radians = degrees * math.pi / 180
               break
           except ValueError:
               print("PLs enter the number !!!")       
        print("Pls wait the result !!!")  
        t.sleep(1)
        print("The radians are: ", radians)
        return radians 
    
    def Radians_To_Degrees(self):
        while True: 
          try: 
             radians = float(input("Enter the radians: "))
             degrees = radians * 180 / math.pi
             break
          except ValueError:
              print("pls enter the number!!")         
        print("Pls wait the result !!!")  
        t.sleep(1)
        print("The degrees are: ", degrees)
        return degrees
    
    def Abs(self):
        while True:
             try:
                num = int(input("Pls enter the number : "))
                if (num < 0):
                    num = num * -1                            
                break
             except ValueError:
                print("Pls enter the number !!")         
        print("Pls wait the result !!!")
        t.sleep(1)
        print("Abs Value = ",num)
        return num
         
    def Quit(self):
        print("Good bye\nI will look forward to you coming back")          
                    
    def Owner(self):
        print("This program wrote by Mert\nEnjoy the program :)")  
               
calc = Calculator()             

while calc:
    calc.start()