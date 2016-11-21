#!/usr/bin/python
#--*-- coding:utf-8 --*--

def bubble_sort(a):
    for i in range(len(a)):
        tmp = a[i]
        for j in range(i+1, len(a)):
            if a[j] < tmp:
                (a[j], tmp) = (tmp, a[j])
        a[i] = tmp

if __name__ == "__main__":
    a = [12, 21, 1, 42, 14, 42, 56,21]
    print "before sort:"
    print a
    bubble_sort(a)
    print "after sort:"
    print a

