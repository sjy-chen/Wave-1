#asking for dimensions in feet from user
length = input("Enter the length of the field in feet: ")
width = input("Enter the width of the field in feet: ")

#converting length/width to floats
length = float(length)
width = float(width)

#finding area in square feet
area_in_square_feet = length*width

#converting area in square feet to acres
area_in_acres = area_in_square_feet / 43560

#converting to string
area_in_acres = str(area_in_acres)

#printing out the result to the user(concatenation)
print("The area of the field is " + area_in_acres + " acres.")