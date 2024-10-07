num1=float(input("Enter the first numeber:"))
op=input("Enter the operation:")
num2=float(input("Enter the second number:"))
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("Invalid operation")
