#!/usr/bin/env python
#--*-- coding:utf-8 --*--

#取中间数，比较关键字，根据大小改变左右下标，递归再次比较关键字和中间数的大小，直至找到或者找完数组

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

