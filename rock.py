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
import random
image =[rock,paper,scissors]
user_choice = int(input('enter 0 for rock,1 for papper,2 for scissors '))
if user_choice>=3 or user_choice<0:
    print('invalid number,you lose!')
else:
    print(image[user_choice])
    computer_choice =random.randint(0,2)
    print(image[computer_choice])
    if user_choice ==0 and computer_choice ==2:
        print('you win!')
    elif user_choice ==2 and computer_choice ==0:
        print('you lose!')
    elif computer_choice>user_choice:
        print('you lose!')
    elif user_choice>computer_choice:
        print('you win!')
    elif user_choice == computer_choice:
        print('its a draw')
