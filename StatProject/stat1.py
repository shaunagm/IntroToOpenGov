import csv

with open('contributions.csv', 'rb') as csvfile:
	contributions = csv.reader(csvfile, delimiter=',')
	for row in contributions:
		print "Amount: ",row[0]," Recipient: ",row[7]


## Comments (remove and place in instructor guide before event)
## This file introduces/demonstrates:
#    # Reading in information via csvreader
#    # Iterating through data with a for loop
#    # Using (in this case printing) selected elements from an array

## Concepts to touch on:
#    #  Delimiter parameter in csv.reader. 
#    #  Python is 0-indexed, not 1-indexed.

## Customization:
#    #  Have students play around with displayed: what amounts are shown and how?
