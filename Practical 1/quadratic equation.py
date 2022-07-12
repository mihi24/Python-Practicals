#quadratic equation
import math
a= int(input("Enter the value of a "))
b= int(input("Enter the value of b "))
c= int(input("Enter the value of c "))
dis = (b**2 - 4*a*c)**0.5
res1 = (-b + dis)/2*a
res2 = (-b - dis)/2*a

print("Values are ", res1,res2)