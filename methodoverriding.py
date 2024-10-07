class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)


    def area(self):
        return 3.14*super().area()#if the method area is not presented here,
        # the desired output for cirlce won't come and if we create an super
        # method but not area method it will give the area of rectagnle instead\
        # of circle so to get desired output we use super method again in area method of derived class
        #this is called method overriding we used area of shape class in derived class
        # using super method


rec=shape(5,5)
print(rec.area())
c=circle(4)
print(c.area())