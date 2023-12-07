import time as t

print("\n\n----- Welcome To The Grade Calculator -----\n")

name = input("Please enter your name: ")

answer = input(f"\nDo you want to calculate your grade {name}? (y/n)\nAnswer: ")

lesson_names = list()

grades = list()

if(answer == 'y'):
    
    number = int(input("\nHow many course names will you enter?\nAnswer: "))
    
    inital = 1
    
    while inital <= number:
        
        lesson = input(f"\nPlease enter the name of lesson {inital}: ")
        
        inital += 1
        
        lesson_names.append(lesson)
          
        midterm = int(input("Please enter midterm exam: "))

        if(midterm < 0 or midterm > 100):
            
            print("\nInvalid input for midterm. Please re-enter. Please enter exam point between 0-100")
            
            midterm = int(input("Please enter midterm exam: "))
            
        final = int(input("Please enter final exam: "))

        if(final < 0 or final > 100):
            
            print("\nInvalid input for final. Please re-enter. Please enter exam point between 0-100")
            
            final = int(input("Please enter final exam: "))
            
        result = (midterm * 4) / 10 + (final * 6) / 10

        print("Your grade is calculating...")
    
        t.sleep(1.5)
        
        grades.append(result)
    
    print("\nPlease waiting the result...")
        
    t.sleep(1.5)
        
    print("\nLessons\t\tGrades\n-------\t\t------\n")
    
    for i,j in zip(lesson_names,grades):

        print(f"{i}\t\t{j}\n")

if(answer == 'n'):
    
    print("\nExiting the system...")
    
    t.sleep(1.5) 
    
    print(f"Good Bye {name.capitalize()} :)\n")  