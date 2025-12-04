import os
from random import randint
from time import sleep

def clear():
  os.system('cls')

#######    Your code here    #######

score = 100
playCost = 5
totalPayout = 0
wannaPlay = True

slots = [[1,2,3],[4,5,6],[7,8,9]]
payouts = [5, 25, 50, 50, 50, 50, 100, 80, 45, 66]

print("Welcome to Dizzy Slots!")
sleep(1)
input("Press enter to start!")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #the clear thing kept breaking, saying "cls is not defined," so this is what you get for now
while wannaPlay and score > 0:
  score = score - playCost
  for row in slots:
    for num in row:
      
  placeholderInput = input("Roll again? *yes/no* : ")
  if placeholderInput.lower() != "yes":
    break
  



print("Thanks for playing!")

#score += payouts[num-1] * mod
#for row in slots:
#    for num in row:
#        print(f"|{num}|", end="")
#    print()