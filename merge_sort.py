#!/usr/bin/env python
#--*-- coding:utf-8 --*--


def merge(a, low, mid, high):
    b = []
    i = low 
    j = mid + 1 
    while i < mid +1 and j <= high:
        if a[i] <= a[j]:
            b.append(a[i])
            i += 1
        else:
            b.append(a[j])
            j += 1
    while i < mid+1:
        b.append(a[i])
        i += 1
    while j <= high:
        b.append(a[j])
        j += 1
    print b
    for i in range(0,len(b)):
        a[i] = b[i]


def merge_sort(a, left, right):
    if left == right:
        return
    mid = (left + right)/2
    merge_sort(a, left, mid)
    merge_sort(a, mid+1, right)
    merge(a, left, mid, right)


if __name__ == "__main__":
    a = [11, 2, 32, 76, 27, 53, 49]
    #a = [1, 3,5,7,2,4,8]
    print "before merge"
    print a
    merge_sort(a, 0, len(a)-1)
    #merge(a, 0, (len(a)-1)/2, len(a)-1)
    print "after merge"
    print a
