i=int(input("Enter the number:"))
original=i
reversed_num=0
while i!=0:
    rem=i%10
    reversed_num=(reversed_num*10+rem)
    i//=10
print("The reversed number: ",(reversed_num))
if original==reversed_num:
    print("The number is palindrome")
else:
    print("The number is not palindrome")


# mom -> palindrome
# binit -> not palindrome