# a=float(input("Enter the first number:"))
# b=float(input("Enter the second number:"))
# c=float(input("Enter the third number:"))
# if (a >=b) and (a >= c):
#  largest=a # you will get an error
# elif (b >= a) and (b >= c):
#  largest=b
# else:
#  largest=c
# print("The largest value is",largest)
#using function
def max(num1,num2,num3):
  if (num1>=num2)and(num2>=num3):
    return num1
  elif(num2>=num1) and (num2>=num3):
    return num2
  else:
    return num3
print(max(4,6,7))

