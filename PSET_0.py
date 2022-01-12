##################################################
##  Problem 1. common
##################################################

# Given an array of lists of distinct numbers, 
# return the number of numbers common to all lists

def common(lists):
    '''
    Input:  lists  | Array of arrays of positive integers
    Output: num_common  | number of numbers common to all arrays
    '''
    if len(lists) < 1 or not lists[0]:
        return 0
    common_set = set(lists[0])
    for l in lists[1:]:
        common_set = common_set.intersection(set(l))
    return len(common_set)

