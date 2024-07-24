import random

def guess_game():
    print("Welcome to NUMBER GUESSING Game.")
    print("Compute have selected secret number between 1 and 100. Please guess the number.:")
    
#generate random number between 1 and 100
    secret_number=random.randint(1,100)
    attempt=0
   
    while True:
        guess=int(input("Enter Your guess between 1 and 100: "))
        attempt +=1
        
        if guess<secret_number:
            print("Your guess is too low. Please guess again. ")
            
        elif guess>secret_number:
            print("Your guess is too high. Please guess again. ")
            
        else:
            print(f"Congratulations! your guess {guess} is correct. ")
            print(f"You did it in {attempt} attempts.")
            break
        
if __name__=="__main__":
    guess_game()