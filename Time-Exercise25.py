#asking number of seconds from user
original_seconds = input("Enter a number of seconds: ")

#convert the value to an integer
seconds = int(original_seconds)

#calculate the number of seconds in a day
days = int(seconds / 86400)
seconds = seconds % 86400

#calculate the number of seconds in an hour
hours = int(seconds / 3600)
seconds = seconds % 3600

#calculate the number of seconds in a minute
minutes = int(seconds / 60)
seconds = seconds % 60

#print output to user(concatenation)
print("In the format D:HH:MM:SS, " + original_seconds + " seconds can be written as " + "%d:%02d:%02d:%02d." % (days, hours, minutes, seconds))