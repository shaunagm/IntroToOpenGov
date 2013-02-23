### This example uses the pandas library to repeat some of the same operations.
### Pandas is a very powerful data-manipulation library that takes some time to learn.
### http://pandas.pydata.org/

import pandas as pd
import scipy.stats as scipy

# Read the contributions file into a pandas DataFrame
# The parse_dates argument will make it convert the date column correctly
contributions = pd.io.parsers.read_csv('contributions.csv', parse_dates=[1])

# Look at the data a bit
print contributions.head()

# Individual rows can be accessed with .ix
print contributions.ix[3]

# stat1.py
# iterrows() gives pairs of index, data
#for index, row in contributions.iterrows():
#    print "Amount: ", row['amount'], " Recipient: ", row['recipient_name'])

# stat3.py
# Pandas doesn't make you choose between row-wise and column-wise access
print contributions.amount.sum()

# stat4.py
# pandas supports simple statistics on columns
print "Maximum value: ", contributions.amount.max()
print "Minimum value: ", contributions.amount.min()
print "Mean value: ", contributions.amount.mean()
print "Median value: ", contributions.amount.median()
print "Range: ", abs(contributions.amount.max() - contributions.amount.min())

# stat5.py
# Pandas has very flexible indexing
# Here we use a boolean value to select amounts for each party
rep_amounts = contributions.amount[contributions.recipient_party=='R']
dem_amounts = contributions.amount[contributions.recipient_party=='D']

# The t-test is performed the same way using scipy
[t,p] = scipy.ttest_ind(rep_amounts, dem_amounts)

print "t:",t,"p:", p

c=contributions
