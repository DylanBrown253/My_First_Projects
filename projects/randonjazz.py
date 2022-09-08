import random as random
guesses = 0
top_of_range = input("Pick the pool of numbers(Ex. 20): ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <=0 :
        print("Please chose a number greater then zero! ")
else :
    print("Please chose a number next time! ")
    quit()
random_number = random.randint(0, top_of_range)
while True :
    
    user_guess = input("Please Choose a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else :
        print("Please chose a number next time! ")
        continue
    if user_guess == random_number:
        print("Good guess! ")
        break
    else :
        guesses=+1
        if user_guess > random_number:
            print("Guess lower! ")
        else : 
            print("Guess Higher! ")
print("You won in", guesses, "Guesses")

        

 