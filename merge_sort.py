#!/usr/bin/env python
#--*-- coding:utf-8 --*--


def merge(a, low, mid, high):
    b = []
    i = low 
    j = mid + 1 
    while i <= mid  and j <= high:
        if a[i] <= a[j]:
            b.append(a[i])
            i += 1
        else:
            b.append(a[j])
            j += 1
    while i <= mid:
        b.append(a[i])
        i += 1
    while j <= high:
        b.append(a[j])
        j += 1
    for i in range(0,len(b)):
        a[low] = b[i]
        low += 1


def merge_sort(a, left, right):
    if left == right:
        return
    mid = (left + right)/2
    merge_sort(a, left, mid)
    merge_sort(a, mid+1, right)
    merge(a, left, mid, right)

if __name__ == "__main__":
    a = [11, 2, 32, 76, 27, 53, 49]
    print "before merge"
    print a
    merge_sort(a, 0, len(a)-1)
    print "after merge"
    print a
