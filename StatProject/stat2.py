import csv

data = []

with open('contributions.csv', 'rb') as csvfile:
	contributions = csv.reader(csvfile, delimiter=',')
	for row in contributions:
		data.append([int(row[0]),row[7]])

print data
print "Final row: ", data[len(data)-1]

## Thoughts:
#  I think numpy turned out to be overkill?  Moved to scrap.

# Introduces/exemplifies
#    #  Lists and how they hold multiple data types and how to index within them.
#    #  Initializing a variable before adding to it?  (Instructors can show
#    #  what happens if you comment that out.
#    #  Converting from string to number.
#    #  Finding the final element of a matrix/array/list by getting len - 1.

