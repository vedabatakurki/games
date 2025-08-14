# rock paper scissor
# rock 0 paper 1 scissor 2
# rock wins against scissor
# scissor wins against paper
# paper wins against rock
# combinations you vs computer win
#              0        0     draw
#              0        1     computer
#              0        2     you
#              1         0    you
#              1         1    draw
#              1        2       computer
#              2        0       computer
#             2         1      you
#            2          2      draw

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
---'    ____)____
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

images = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}


choices = ["rock", "paper", "scissors"]
user_input=int(input("enter a number between 0 1 and 2:"))
print("you choose", choices[user_input])
print(images[choices[user_input]])
computer_input=random.randint(0,2)
print("computer choose",end=' ')
print(computer_input)
print("computer choose", choices[computer_input])
# print(rps_images.images[choices[computer_input]])
if user_input>=3:
    print("just exit")
else:
    if user_input==computer_input:
        print("draw")
    elif user_input==2 and computer_input==0:
        print("computer wins")
    elif user_input==0 and computer_input==2:
        print("you won")
    elif user_input>computer_input:
        print("you won")
    elif computer_input>user_input:
        print("computer won")