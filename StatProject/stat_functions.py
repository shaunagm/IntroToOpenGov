#!python



############################################################################
def median(data_array):
    data_sorted = data_array[:] # make a copy of the list
    data_sorted.sort() # in-place sort
    num_values = len(data_sorted)
    half = num_values // 2  # floored quotient
    if num_values % 2: # modulo 2, odd if true
        median = data_sorted[half] # 0-index list
    else:
        median = (data_sorted[half-1] + data_sorted[half]) / 2.0
    return median


def minimum(data_array):
    data_sorted = data_array[:] # make a copy of the list
    data_sorted.sort() # in-place sort
    return data_sorted[0] # first value in the list

def maximum(data_array):
    data_sorted = data_array[:] # make a copy of the list
    data_sorted.sort() # in-place sort
    return data_sorted[-1] # last value in the list

def data_range(data_array):
    return maximum(data_array) - minimum(data_array)


def mean(data_array):
    # if the data is all integers, the mean should still be a float
    total = 0.0
    for val in data_array:
        total += val
    mean = total / len(data_array)
    return mean


############################################################################
def print_values(data_set):
    print "Maximum value: ", maximum(data_set)
    print "Minimum value: ", minimum(data_set)
    print "Mean value: ", mean(data_set)
    print "Median value: ", median(data_set)
    print "Range: ", data_range(data_set)


############################################################################
if __name__ == "__main__":
    data_test = [1, 2, 3, 4, 7]
    print_values(data_test)

    data_test = [1, 2, 3, 4, 5, 7]
    print_values(data_test)

