import csv

with open('contributions.csv', 'rb') as csvfile:
	contributions = csv.reader(csvfile, delimiter=',')
	for row in contributions:


## Thoughts:
# What's the best way to minimally/easily show students how to make a data
# structure?  Arrays and dicts don't seem ideal, AL suggests numpy.
