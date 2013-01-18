import csv
import math 

# Using the two-list structure...
data_amounts = []
data_recipients = []
with open('contributions.csv', 'rb') as csvfile:
        contributions = csv.reader(csvfile, delimiter=',')
        next(contributions)
        for row in contributions:
                data_amounts.append(int(row[0]))
		data_recipients.append(row[7])

# Using standard python functions (and a little bit of creativity)
print "Maximum value: ",max(data_amounts)
print "Minimum value: ",min(data_amounts)
print "Mean value: ", sum(data_amounts)/len(data_amounts)
print "Median value: ", data_amounts[len(data_amounts)/2]
print "Range: ", abs(max(data_amounts) - min(data_amounts))



