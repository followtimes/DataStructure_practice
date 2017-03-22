#!/usr/bin/env python
#--*-- coding: utf-8 --*--


def merge(a, left, mid, right):
    low = left
    high = mid + 1
    tmp = []
    while low <= mid and high <= right:
        if a[low] <= a[high]:
            tmp.append(a[low])
            low += 1
        else:
            tmp.append(a[high])
            high += 1
    while low <= mid:
        tmp.append(a[low])
        low += 1
    while high <= right:
        tmp.append(a[high])
        high += 1
    cnt = 0
    while cnt < len(tmp):
        a[left] = tmp[cnt]
        cnt += 1
        left += 1

def merge_sort(a, left, right):
    if left < right:
        mid = (left + right) / 2
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
