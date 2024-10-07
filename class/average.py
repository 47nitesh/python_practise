class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks =marks
        # print(name,marks)
    def average(self):
     sum=0
     for x in self.marks:
         sum+=x
     print("Hello",self.name,"Your average is",sum/3)
s1=student("Manis",[96,92,91])
s1.average()
s1.name="Nitesh"
s1.marks=[46,78,99]
s1.average()






