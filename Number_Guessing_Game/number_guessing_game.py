import random

print("----------------------------------------------")
print("              Number Guessing Game            ")
print("----------------------------------------------\n")

while(True):
    num=random.randint(1,100)
    count=0
    guessed=False

    print("Hello ! welcome to the Number Guessing Game ")
    print("I have chosen a number between 1 to 100")
    print("Try to guess it ")

    while(count<10):
        try:
            guess=int(input("\nGuess the number :"))
            if(guess<1 or guess>100):
                print("Please enter a number between 1 to 100 \n")
                continue
        except ValueError:
            print("Invalid input! Please enter a number \n")
            continue
        
        count+=1
                  
        if(guess==num):
            print("Congrats! you guessed it \n")
            guessed=True
            break
        elif(guess<num):
            print("Too low")
        elif(guess>num):
            print("Too high")
            
        print(count, "Attempt of ",10)

       
    if(guessed==False):
        print("Oh-oh looks like you didn't guess the number correctly") 
        print("The number is ",num)

    choice=input("\nDo you want to continue the game (yes/no)?").lower()
    
    if(choice!="yes"):
      print("\nThank you for playing ")
      break


print("----------------------------------------------")
    
