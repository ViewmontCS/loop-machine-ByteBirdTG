import os
from random import randint
from time import sleep

def clear():
  os.system('cls')

#######    Your code here    #######

score = 100
playCost = 5
payouts = [25, 25, 25, 80, 80, 50, 50, 50, 100, 66]


print("Welcome to Dizzy Slots!")
sleep(1)
input("Press enter to start!")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #the clear thing kept breaking, saying "cls is not defined," so this is what you get for now
while score > 0:
    slots = [[randint(1,9),randint(1,randint(1,9)),randint(1,9)],[randint(1,9),randint(1,9),randint(1,9)],[randint(1,9),randint(1,9),randint(1,9)]]
    score = score - playCost
    if slots[0][0] == slots[0][1] == slots[0][2]:
      score = score + payouts[0]
    if slots[1][0] == slots[1][1] == slots[1][2]:
      score = score + payouts[1]
    if slots[2][0] == slots[2][1] == slots[2][2]:
      score = score + payouts[2]

    if slots[0][0] == slots[1][1] == slots[2][2]:
      score = score + payouts[3]
    if slots[2][0] == slots[1][1] == slots[0][2]:
      score = score + payouts[4]

    if slots[0][0] == slots[1][0] == slots[2][0]:
      score = score + payouts[5]
    if slots[0][1] == slots[1][1] == slots[2][1]:
      score = score + payouts[6]
    if slots[0][2] == slots[1][2] == slots[2][2]:
      score = score + payouts[7]

    if slots[0][0] == slots[0][1] == slots[0][2] == slots[1][0] == slots[1][1] == slots[1][2] == slots[2][0] == slots[2][1] == slots[2][2]:
      score == score + payouts[8]
#            print(f"|{slots[0]}|\n|{slots[1]}|\n|{slots[2]}|")
#            print(f"|{slots}|\n")
    print(f"|{slots[0][0]}|{slots[0][1]}|{slots[0][2]}|\n|{slots[1][0]}|{slots[1][1]}|{slots[1][2]}|\n|{slots[2][0]}|{slots[2][1]}|{slots[2][2]}|\n")
    print(score)
    if score > 0:
        placeholderInput = input("Play again? *y/n* : ")
        if placeholderInput.lower() != "y":
            break

print("Thanks for playing!")
