import time
time=time.strftime('%H:%M:%S')
hour=int(input("Enter the hour:"))
print(hour)
if(hour>0 and hour<12):
    print("Good morning sir!")
elif(hour>12 and hour<17):
    print("Good afternoon sir !")
else:
    print("Good evening sir")