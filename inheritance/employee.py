class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"The name of employee::{self.id} is {self.name}")
class programmer(employee):
    def show(self):
        print("Hello my name is nitesh")
p1=employee("Samir",121)
p1.showdetails()
p1=programmer("Harry",410) #when you call the def showdetails without
                                    # decalring programmer derived classs
                                    #it will cause an error
p1.showdetails()
p1.show()


