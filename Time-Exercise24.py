#asking for time from user
days = input("Enter the number of days: ")
hours = input("Enter the number of hours: ")
minutes = input("Enter the number of minutes: ")
seconds = input("Enter the number of seconds: ")

#converting values to ints
days = int(days)
hours = int(hours)
minutes = int(minutes)
seconds = int(seconds)

#computing total seconds
total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds

#converting to a string
total_seconds = str(total_seconds)

#printing out the result to user(concatenation)
print("The total number of seconds is " + total_seconds + ".")