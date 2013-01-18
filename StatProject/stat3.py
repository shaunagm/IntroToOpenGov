import csv

# From stat2.py, gets our data and puts it into a matrix.
data = []
with open('contributions.csv', 'rb') as csvfile:
        contributions = csv.reader(csvfile, delimiter=',')
        next(contributions)
        for row in contributions:
                data.append([int(row[0]),row[7]])

#This is how we sum using the data structure we've made.
loop_sum = 0
for row in data:
	loop_sum += row[0]
print "Looping sum: ", loop_sum

#But is there an easier way?  Let's try a different strucutre.
data_amounts = []
data_recipients = []
with open('contributions.csv', 'rb') as csvfile:
        contributions = csv.reader(csvfile, delimiter=',')
        next(contributions)
        for row in contributions:
                data_amounts.append(int(row[0]))
		data_recipients.append(row[7])

# One line!
print "Summing a list:", sum(data_amounts)



#### Thoughts
#    # Is it a good idea to show multiple ways to do this, or will it be 
#    # confusing?  Maybe put them in two files?

#  Introduces/Exemplifies:
#  next() -- why do we skip the first iteration?
#  manual sums, list sums
