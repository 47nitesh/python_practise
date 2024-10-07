import random
user_choice=int(input("Enter 0 for Rock,1 for paper,2 for scissors:"))
comp_choice=(random.randint(0,2))

print("Computer choose "+ str(comp_choice))
if user_choice > int(3):
    print("Its an invalid choices ....Please try again")
if user_choice > comp_choice:
    print("You Win!")
elif user_choice==0 and comp_choice==2:
    print("You Win!")
elif user_choice==2 and comp_choice==0:
    print("You lose")
elif user_choice<comp_choice:
    print("You lose")
elif user_choice==comp_choice:
    print("Its a draw")