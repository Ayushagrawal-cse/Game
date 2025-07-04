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


game_images=[rock,paper,scissors]

user_score=0
computer_score=0
while True:
    user_input = input("Choose 0 for Rock, 1 for Paper, 2 for Scissors or 'q' to quit: ")
    if user_input=='q':
        break
    if user_input not in ['0', '1', '2']:
        print("Invalid input. Try again.")
        print(f"Final Score: You = {user_score}, Computer = {computer_score}")
        continue

    user_choice=int(user_input)
    print(f"user choose:{user_choice}")
    print(game_images[user_choice])

    computer_choice=random.randint(0,2)
    print(f"computer choose:{computer_choice}")
    print(game_images[computer_choice])



    if user_choice==0 and computer_choice==2:
        print("you win")
        user_score=user_score+1
    elif computer_choice==0 and user_choice==2:
        print("you lose")
        computer_score=computer_score+1
    elif computer_choice>user_choice:
        print("you lose")
        computer_score=computer_score+1
    elif user_choice> computer_choice:
        print("you win")
        user_score=user_score+1
    elif computer_choice==user_choice:
        print("draw")
print("\nGame Over!")
print(f"Final Score: You = {user_score}, Computer = {computer_score}")

    

