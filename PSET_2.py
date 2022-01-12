##################################################
# Problem Set 2 Coding Problem: Happy Accidents
##################################################

'''
Computes the number of happy accidents for an input array.
A happy accident is defined as a pair of values (i, j) in the 
array where i is positioned to the left of j and i > j.
You may assume all values are distinct.

param:arr: list[int] input array
returns:int: the number of happy accidents
'''
import math

def count_happy_accidents(arr):  
    return rec_happy_accidents(arr)[1]

def rec_happy_accidents(ord):
    """
    Takes a list and splits it, theen recursively calls and merges while counting acc
    returns (ordered list, accident count)
    """
    count = 0
    output = []
    lng = len(ord)
    if lng < 2:
        return (ord,0)
    k = l_size = math.ceil(lng/2)
    r_size = math.floor(lng/2)
    l,l_count = rec_happy_accidents(ord[:l_size])
    r,r_count = rec_happy_accidents(ord[l_size:])
    l_ind = 0
    r_ind = 0
    count += l_count + r_count
    while l_ind < l_size and r_ind < r_size:
        if l[l_ind] > r[r_ind]:
            count += k
            output.append(r[r_ind])
            r_ind += 1
        else:
            k -= 1
            output.append(l[l_ind])
            l_ind += 1
    while l_ind < l_size:
        output.append(l[l_ind])
        l_ind += 1
    while r_ind < r_size:
        output.append(r[r_ind])
        r_ind += 1
    return (output,count)
        





