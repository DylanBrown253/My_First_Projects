import colorama
from colorama import Fore
colorama.init(autoreset=True)
name = input(Fore.MAGENTA + "What is your name: ")
print(Fore.WHITE + "What's good", name, "welcome to my adventure")
answer = input("You are on a dirtroad, it has come to an end and you can go left or right. Which way would you like to go? ").lower()
if answer == "left":
    answer = input("You come to a river you can walk around it or you can swim across? ").lower()
    if answer == "walk":
        answer = input("You see a Mcdonalds do you go inside or keep walking? ").lower()
        if answer == "go inside":
            print(Fore.GREEN + "You ordered two baconMcdoubies and were verry happy! ")
        if answer == "keep walking":
            answer = input("You see a giant redbull can it has 450oz. Do you drink it or leave it? ").lower()
        if answer == "drink it":
                print(Fore.GREEN + "THAT REDBULLY KEEPT YOU GOING AND YOU RAN ALL THE WAY TO BECOME THE LEADER OF CHINA")
        if answer == "leave it":
                print(Fore.GREEN + "You passed out from exhaustion and woke up in 2130. You are fully bionic and can live forever now! ")
    elif answer == "swim":
        print(Fore.RED + "You realized you can't swim! ") 
elif answer == "right":
    answer = input("You see a minicopter taking off and also see Andrew Tate. Do you become the top G or do you fly away?(fly/top g) ").lower()
    if answer == "fly":
        answer = input("Great choice. But the top G is pissed and after us. Do you parachute out or go full speed? ").lower()
        if answer == "parachute":
            print(Fore.RED + "You landed in the desert and died")
        elif answer == "full speed":
            print(Fore.GREEN + "Nice work obviously Andrew Tate can't do anything if we are flying in the air right? ***SHORTLY AFTER ANDREW TATE SENT AN RPG TO THE HELICOPTER***")
    elif answer =="top g":
        print(Fore.RED + "Andrew actually thinks your a fag! So you got taken out! ")
else: 
    print(Fore.RED + "Not possible. You lost! ")
print(Fore.GREEN + "Thanks for playing!")