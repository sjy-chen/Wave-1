#asking for cents from user
cents = input("Enter the number of cents: ")

#converting cents to float
cents = float(cents)

#determining number of toonies
toonies = cents // 200
cents = cents % 200

#determining number of loonies
loonies = cents // 100
cents = cents % 100

#determining number of quarters
quarters = cents // 25
cents = cents % 25

#determining number of dimes
dimes = cents // 10
cents = cents % 10

#determining number of nickels
nickels = cents // 5
cents = cents % 5

#determing number of pennies
pennies = cents

#converting values to ints
toonies = int(toonies)
loonies = int(loonies)
quarters = int(quarters)
dimes = int(dimes)
nickels = int(nickels)
pennies = int(pennies)

#converting values to strings
toonies = str(toonies)
loonies = str(loonies)
quarters = str(quarters)
dimes = str(dimes)
nickels = str(nickels)
pennies = str(pennies)

#printing out result to the user (concatenation)
print("The amount of change given should be:")
print(toonies + " toonies")
print(loonies + " loonies")
print(quarters + " quarters")
print(dimes + " dimes")
print(nickels + " nickels")
print(pennies + " pennies")