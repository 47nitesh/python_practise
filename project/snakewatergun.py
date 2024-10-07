import random
comp=random.randint(0,2)
print("Welcome to the snake water and gun game!")
user=int(input("Enter 0 for snake,1 for water and 2 for gun:"))
def check():
    if(comp==user):
        return 0
    elif(comp==0 and user==1):
        return 1                      #comp wins
    elif (comp == 2 and user ==0):
        return 2                       #comp win
    elif(comp==2 and user==1):
        return 3
                                       #user wins
    elif(user==2  and comp==1):
        return 4                       #comp wins

compchoice=comp
print("Computer choosed:",compchoice)
show=check()
if(show==0):
    print("Its a draw")
elif(show==1):
    print("Comp wins")
elif(show==2):
    print("Comp wins")
elif(show==3):
    print("user wins")
elif(show==4):
    print("comp wins")
