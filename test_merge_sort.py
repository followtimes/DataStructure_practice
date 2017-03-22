#!/usr/bin/env python
#--*-- coding: utf-8 --*--


def merge(a, left, mid, right):
    low = left
    high = right
    tmp = []
    while low < mid and high >= mid:
        if a[low] <= a[mid]:
            tmp.append(a[low])
            low += 1
        else:
            tmp.append(a[mid])
            mid += 1
    while low < mid:
        tmp.append(a[low])
        low += 1
    while high >= mid:
        tmp.append(a[mid])
        mid += 1
    cnt = 0
    while cnt < len(tmp):
        a[left] = a[cnt]
        cnt += 1
        left += 1

def merge_sort(a, left, right):
    mid = (left + right) / 2
    if left < right:
        merge_sort(a, left, mid)
        merge_sort(a, mid+1, right)
        merge(a, left, mid, right)


a = [12, 22, 32, 12, 11, 20, 32, 44]
print "before sort:"
print a
merge_sort(a, 0, len(a)-1)
print "after sort:"
print a
