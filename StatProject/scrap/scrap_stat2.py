import csv
import numpy

data = ["amount","recipient"]

with open('contributions.csv', 'rb') as csvfile:
	contributions = csv.reader(csvfile, delimiter=',')
	for row in contributions:
		data = numpy.vstack([data,int([row[0]),row[7]]])

print data
print "Final row: ", data[data.shape[0]-1,]

## Thoughts:
#  Is this the best way to build the data structure?  Is this the best way
#  to show how to build this data structure?  Is that final print shape too
#  complicated?  Also, the headers for data are whack.


# Introduces/exemplifies
#    #  Importing from libraries (csv, numpy)
#    #  Initializing a variable before adding to it?  (Instructors can show
#    #  what happens if you comment that out.
#    #  Vstack...
#    #  Converting from string to number.
#    #  Indexing into arrays.
#    #  Finding the final element of a matrix/array/list by getting size - 1.

