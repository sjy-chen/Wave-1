length = float(input("Enter the length of the field in feet: "))
width = float(input("Enter the width of the field in feet: "))
area_in_square_feet = length*width
area_in_acres = area_in_square_feet / 43560
print("The area of the field in acres is " + str(area_in_acres) + " acres.")