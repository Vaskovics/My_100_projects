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
choices = rock, paper, scissors

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
print(user_choice)
print(choices[user_choice])
print("Computer chose:")
print(choices[computer_choice])
if user_choice == 0:
    if computer_choice == 0:
        print("Draw!")
    elif computer_choice == 1:
        print("You lost!")
    else:
        print("You win!")
elif user_choice == 1:
    if computer_choice == 0:
        print("You win!")
    elif computer_choice == 1:
        print("Draw!")
    else:
        print("You lost")
elif user_choice == 2:
    if computer_choice == 0:
        print("You lost!")
    elif computer_choice == 1:
        print( "You win!")
    else:
        print("Draw!")