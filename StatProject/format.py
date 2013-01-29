##### Create simple function using text from stat3.py that inputs the data from a csv file
##### and outputs two-list data structure using specified columns.

import csv

def format(datafile, col1, col2):
	col1_array = []
	col2_array = []
	with open(datafile, 'rb') as csvfile:
        	contributions = csv.reader(csvfile, delimiter=',')
        	next(contributions)
        	for row in contributions:
                	col1_array.append(int(row[col1]))
                	col2_array.append(row[col2])
	return col1_array,col2_array
