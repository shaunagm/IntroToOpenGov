import csv
import math 
import format

# Using our new format function to create the two-list structure...
[data_amounts, data_recipients] = format.format('contributions.csv',0,7)

# Using standard python functions (and a little bit of creativity)
print "Maximum value: ",max(data_amounts)
print "Minimum value: ",min(data_amounts)
print "Mean value: ", sum(data_amounts)/len(data_amounts)
print "Median value: ", data_amounts[len(data_amounts)/2]
print "Range: ", abs(max(data_amounts) - min(data_amounts))



