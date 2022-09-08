import random 
user_wins = 0
bot_wins = 0
ties = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in ["rock", "paper", "scissors"]:
        continue
    
    random_number = random.randint(0, 2)
    # rock is: 0, paper is: 1, scissors is: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick +".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won! ")
        user_wins +=1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You won! ")
        user_wins +=1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won! ")
        user_wins +=1
    elif user_input == computer_pick:
        print("Tie! ")
        ties +=1
    else: 
        print("You lost! ")
        bot_wins +=1
    
print("You won", user_wins, "times! ")
print("The computer won", bot_wins, "times! ")
print("Also you tied", ties, "times! ")
        



    
print("Goodbye")

