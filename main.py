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
options =[rock,paper,scissors]
user_chioce = input('what you what to choose? 0 for rock , 1 paper ,2 scissors ? ')
user_chioce_in_integer = int(user_chioce)
import random
user_chioce_in_figer = options[user_chioce_in_integer]
random_number = random.randint(0,2)
print(f"{user_chioce_in_figer} \n you choose")
computer_choice = options[random_number]
print(f"{computer_choice}  \n  Computer Choice")
if random_number >= 3 or user_chioce_in_integer < 0: 
  print("You typed an invalid number, you lose!") 
elif user_chioce_in_integer == 0 and random_number == 2:
  print("You win!")
elif random_number == 0 and user_chioce_in_integer == 2:
  print("You lose")
elif random_number > user_chioce_in_integer:
  print("You lose")
elif user_chioce_in_integer > random_number:
  print("You win!")
elif random_number == user_chioce_in_integer:
  print("It's a draw")