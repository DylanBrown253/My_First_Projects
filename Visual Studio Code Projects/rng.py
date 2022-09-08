import random as random
print ("What do you think the number will be? ")
answer = input("Your guess here.--> ")
if answer.isdigit():
    answer = int(answer)
    if answer <= 0 :
        print("please choose a number greater then zero! ")
        quit()
else :
    print("Please type a number next time")
    quit()

randomrange = random.randrange(1,10)
print(randomrange)
if answer == randomrange: 
    print("Good Guess! ")
else :
    print("Try again! ")
    print ("What do you think the number will be? ")
answer = input("Your guess here.--> ")
 


