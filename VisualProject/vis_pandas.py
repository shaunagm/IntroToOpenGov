from __future__ import print_function

### This example uses the pandas library to do some simple visualizations.
### Pandas is a very powerful data-manipulation library that takes some time to learn.
### http://pandas.pydata.org/

import matplotlib.pyplot as plt
import pandas as pd

# Read the contributions file into a pandas DataFrame
# The parse_dates argument will make it convert the date column correctly
contributions = pd.io.parsers.read_csv('contributions.csv', parse_dates=[1])

# Histogram of all contributions
contributions.amount.hist(bins=30)
plt.title('All contributions')

# Box plot of contribution amount stratified by party
contributions.boxplot(column=['amount'], by='recipient_party')

# Same thing but stratified by state
contributions.boxplot(column=['amount'], by='recipient_state')

# Wait until all plot windows are closed
plt.show()
