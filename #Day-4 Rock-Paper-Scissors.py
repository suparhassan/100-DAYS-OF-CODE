#Day-4 Rock Paper Scissors by supar


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print("Welcome to Rock, Paper, Scissors. \n by supar")

user_choice = (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

x = int(user_choice)

outcomes = [rock, paper, scissors]

print(outcomes[x])

print("Computer chose")

CP = random.randint(0,2)

print (outcomes[CP])

if user_choice == 0 and CP == 2:
    print("you win! ;) ")
elif user_choice == 1 and CP == 0:
    print("you win! ;) ")
elif user_choice == 2 and CP == 1:
    print("you win! ;) ")
elif user_choice == CP:
    print("Its a draw!")
else:
     print("Computer Wins :( ")