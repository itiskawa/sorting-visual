import math
import numpy

from numpy import random

def mergesort(A,  left, right):
    if left < right:
        res = [0]*len(A)
        mid = (left+right)//2
        mergesort(A, left, mid)
        mergesort(A, mid+1, right)
        res = merge(A, res, left, mid, right)
    
        return res
    else:
        return None
def merge(A, array, left, mid, right):
    #res = [0]*len(A)
    l = left
    q = mid + 1
    k = left
    
    
    # when not sorted
    
    while l <= mid and q <= right:
        #no inversion
        if A[l] <= A[q]: 
            array[k] = A[l]
            l = l + 1
            k = k + 1
        # swap happens
        else:
            array[k] = A[q]
            q = q + 1
            k = k + 1
        
    #if beginning is ok
    while l <= mid:
        array[k] = A[l]
        k = k + 1
        l = l + 1

    while q <= right:
        array[k] = A[q]
        k = k + 1
        q = q + 1

    #need to modify orignial array so recursive calls don't do the job twice
    for x in range(left, right + 1):
	    A[x] = array[x]

    #print("A", A)
    return A


# random testing
numpy.random.seed
l = numpy.random.randint(0, 350, 1000)

print(sorted(l) == mergesort(l, 0, len(l)-1))