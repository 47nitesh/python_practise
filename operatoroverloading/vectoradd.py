class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
            return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self,other):
      return (f"{self.i+other.i}i+ {self.j+other.j}j+{self.k+other.k}k")

p1=vector(2,3,4)
p2=vector(3,5,6)
c= p1+ p2
print(c)

#another way
class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, other):
        new_i = self.i + other.i
        new_j = self.j + other.j
        new_k = self.k + other.k
        return vector(new_i, new_j, new_k)


# Example usage:
p1 = vector(2, 3, 4)
p2 = vector(3, 5, 6)

c = p1 + p2  # This will call p1.__add__(p2)
print(c)  # Output should be "5i + 8j + 10k"
