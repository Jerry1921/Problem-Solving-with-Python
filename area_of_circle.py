'''from math import pi

r = float(input("write the radius of the circle : \n"))
print("the area of the circle whose radius " + str(r) + " is: " + str(pi *r**2))'''

# Area of a circle
from math import pi

n = int(input('enter the radius of the circle : '))

def area(r):
    ar = pi*r*r
    print(ar)

area(n)

