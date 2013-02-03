import csv
import math 
import format
#import rpy

## [Link to page with good description of a t-test]
## Run through this briefly if there is interest

##	       (mean of x1 - mean of x2)
## t =                    / 
##   square root of ((variance of X1/n of X1) + (variance of X2/n of X2))

# Get data structure 
[data_amounts,data_recipient_party] = format.format('contributions.csv',0,5)

# Initialize variables
n_of_x1,n_of_x2,sum_of_x1,sum_of_x2 = 0,0,0,0

# Create variables
for i in range(len(data_recipient_party)):
	if (data_recipient_party[i] == "R"):
		n_of_x1 += 1
		sum_of_x1 += data_amounts[i]
	if (data_recipient_party[i] == "D"):
		n_of_x2 += 1
		sum_of_x2 += data_amounts[i]
mean_of_x1 = sum_of_x1/n_of_x1
mean_of_x2 = sum_of_x2/n_of_x2

## Find the variance
# Variance = take the difference of each instance from the mean, square it,
# sum it, and divide by n - 1
sum_of_squares_x1, sum_of_squares_x2 = 0,0
for i in range(len(data_recipient_party)):
	if (data_recipient_party[i] == "R"):
		sum_of_squares_x1 += math.pow((data_amounts[i] - mean_of_x1),2)
	if (data_recipient_party[i] == "D"):
		sum_of_squares_x2 += math.pow((data_amounts[i] - mean_of_x2),2)
variance_of_x1 = sum_of_squares_x1 / (n_of_x1 - 1)
variance_of_x2 = sum_of_squares_x2 / (n_of_x2 - 1)

## Calculate T
t = (mean_of_x1 - mean_of_x2) / math.sqrt((variance_of_x1/n_of_x1) + (variance_of_x2/n_of_x2))

print t






