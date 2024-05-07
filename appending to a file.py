f=open("temp.txt","a+")
# print(f.write("\nMeeting coordinater:Dhiraj Shah"))
# f.write("\nResources manager:Biraj Chapagain")

f.write("my name is binit")
f.seek(0)

print(f.readlines())
# print("hello")
f.close()
