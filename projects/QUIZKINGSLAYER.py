playing = input("How well do you know king slayer Quiz. Do you wanna play? ")

if playing.lower() != "yes":
    quit()

print("Let's play then maggot")
score = 0

answer = input("What color is my 3090ti? ")
if answer.lower() == "red":
    print("Fuck YEAH BABY HELL YEAH FLAMMING RED BICHH FUCK YEA!!!!")
    score+= 1
else :
    print("YOU MUST BE ONE DUMB MOTHERFUCKER TO NOT PICK RED! I LIKE MY SHIT HOT BITCH!!!")
answer = input("WHAT DOES EVER1 CALL ME? ")

if answer.upper() == "KS":
    print("FUCK YEA BABY!")
    score+= 1
else :
    print("IS CYBER TAKING THIS SHIT NO ONE CALLS YOU REAPER DUMBASS!!!")
answer = input("KINGSLAYERS FAVORITE GAME? ")
if answer.upper() == "RUST":
    print("LOVE ME SOME RUST 203 HOURS IN THE PAST TWO WEEKS BABY!")
    score+= 1
else :
    print("I DON'T PLAY ANYTHING ELSE SO DONT EVEN FUCKING ASK!")
answer = input("KS'S FAVORITE DRINK? ")
if answer.upper() == "REDBULL":
    print("FUCK YEAH BABY RED BULLYYYYY!!!! ALL I NEED IS  ME A RED BULLY AND I CAN GO A FULL 48 ON RUST!")
    score+= 1
else :
    print("ONLY OTHER THING I LOVE IS A NESQUICKY SO IF YOU ANSWERED THAT I UNDERSTAND. SIKE BITCH!!!!")
answer = input("WHAT DOES KS DO FOR FUN? ")
if answer.upper() == "RUST":
    print("I DON'T DO ANYTHING OTHER THAN PLAY RUST.")
    score+= 1
else :
    print("TRICK QUESTION BABY I FUCKING LOVE RUST BITCH!")
    

print("son of a bitch you got like " + str(score) + " questions right.")
print("THE DOO-HIKYY ON MY PHONE SAID " + str(score/5*100) + "%")