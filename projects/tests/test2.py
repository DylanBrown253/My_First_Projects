print("Welcome to my computer quiz!")

playing = input("Do you to play? ")

if playing != "yes":
    quit()
    
print("Okay! Let's play")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else: answer ==""       