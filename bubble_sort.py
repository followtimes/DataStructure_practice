#!/usr/bin/python
#--*-- coding:utf-8 --*--

def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(i+1, len(a)):
            if a[i] < a[j]:
                (a[i], a[j]) = (a[j], a[i])
                i += 1

if __name__ == "__main__":
    a = [12, 21, 1, 42, 14, 42, 56,21]
    print "before sort:"
    print a
    bubble_sort(a)
    print "after sort:"
    print a

