import csv
import math 
import format
import scipy.stats as scipy

### Doing more complicated statistics

###Manually -- see ttest.py

## Or use functions from libraries!

# Get data structure 
[data_amounts,data_recipient_party] = format.format('contributions.csv',0,5)

# Create array to feed into t-test function
x1,x2 = [],[]
for i in range(len(data_recipient_party)):
	if (data_recipient_party[i] == "R"):
		x1.append(data_amounts[i])
	if (data_recipient_party[i] == "D"):
		x2.append(data_amounts[i])

# Calculate
[t,p] = scipy.ttest_ind(x1,x2)

print "t: ",t," p: ",p
