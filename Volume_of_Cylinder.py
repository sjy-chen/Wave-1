#importing math module
import math

#asking for radius and height from user
radius = input("Enter the radius of the cylinder in units: ")
height = input("Enter the height of the cylinder in units: ")

#converting the height/radius to floats
radius = float(radius)
height = float(height)

#defining pi
pi = math.pi

#finding volume of cylinder
radius_squared = pow (radius,2)
volume = radius_squared * pi * height

#rounding to one decimal place
volume = round(volume, 1)

#converting to a string
volume = str(volume)

#printing out result to the user (concatenation)
print("The volume of the cylinder is " + volume + " units^3.")