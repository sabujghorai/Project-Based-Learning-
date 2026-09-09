# # WAP in python to find the factorial of a number using math module
import math
# fact = int(input("Enter a number :"))
# print(f"Factorial is : {math.factorial(fact)}")


# # WAP to find the area of a circle using math module
# radius = int(input("Enter the radius :"))
# print(f"Area is : {math.pi*math.pow(radius,2)}")


# # WAP in python program to find the gcd of two numbers using math Module

# a = int(input("Enter A :"))
# b = int(input("Enter B :"))
# print(f"The GCD is : {math.gcd(a,b)}")


# # WAP in python program to find the LCM of two numbers using math Module
# c = int(input("Enter A :"))
# d = int(input("Enter B :"))
# print(f"The GCD is : {math.lcm(c,d)}")


# # WAP to calculate the distance between two coordinates 
# x1 = float(input("X1 :"))
# x2 = float(input("X2 :"))
# y1 = float(input("Y1 :"))
# y2 = float(input("Y2 :"))
# Distance = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
# print(f"Distance is : {Distance}")



# WAP to calculate the roots of the equation
a = int(input("Enter A :"))
b = int(input("Enter B :"))
c = int(input("Enter C :"))

root1 = (-b + (math.sqrt(math.pow(b,2)- 4*a*c))) / (2*a)
root2 = (-b - (math.sqrt(math.pow(b,2)- 4*a*c))) / (2*a)
print(root1,root2)