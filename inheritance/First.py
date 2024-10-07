
class car:
    color="Black"
    def __init__(self,name):
      self.name=name
     # self.model=model
class model(car):
      def __init__(self,name):
         self.name=name
c1=(model("BMW"))
print(c1.name)
print(c1.color)
