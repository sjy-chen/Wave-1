#asking for amount deposited by user
initial_deposit = input("Enter your initial deposit: $")

#converting to float
initial_deposit = float(initial_deposit)

#first year of interest
first_year = initial_deposit * 1.04

#second year of interest
second_year = first_year * 1.04

#third year of interest
third_year = second_year * 1.04

#rounding values
first_year = round(first_year, 2)
second_year = round(second_year, 2)
third_year = round(third_year, 2)

#converting values to strings
first_year = str(first_year)
second_year = str(second_year)
third_year = str(third_year)

#printing result to user (concatentation)
print("The amount in the savings account after 1 year is: $" + first_year)
print("The amount in the savings account after 2 years is: $" + second_year)
print("The amount in the savings account after 3 years is: $" + third_year)