import random

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
# scissors beat paper paper beats rock rock beat scissors
rock_paper_scissors= [rock, paper, scissors]

user_choice = int(input("Which do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Please enter a number from 0 to 2")
print(user_choice)
choice = random.choice(rock_paper_scissors)
print(f"Computer chose:\n{choice}")
index = rock_paper_scissors.index(choice)
print(index)
if user_choice > index:
    print("You win!")
elif user_choice == 0 and index ==2:
    print("You win")
    
elif user_choice == index:
    print("It's a tie!")
else:
    print("You lose!")

