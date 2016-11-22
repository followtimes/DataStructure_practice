#!/usr/bin/env python
#--*-- coding:utf-8 --*--

def binary_find(a, left, right, num):
    if left <= right:
        mid = (left + right)/2
        if a[mid] == num:
            print "find num in index of  %d" %mid
        elif a[mid] > num:
            binary_find(a, left, mid-1, num)
        else:
            binary_find(a, mid+1, right, num)
    else:
        print "no such num"


if __name__ == "__main__":
    a = [1, 4, 20, 76, 99, 123]
    print "array is:"
    print a
    num = int(raw_input("please input a num to find:\n"))
    binary_find(a, 0, len(a) - 1, num)

