#!/usr/bin/python
#--*-- coding:utf-8 --*--

def insert_sort(a):
    for index in range(1, len(a)):
        tmp = a[index]
        index -= 1
        while index >= 0:
            if a[index] > tmp :
                a[index+1] = a[index] 
                index -= 1
            else:
                break
        a [index+1] = tmp

if __name__ == "__main__":
    a = [12, 21, 1, 42, 14, 42, 56,21]
    print "before sort:"
    print a
    insert_sort(a)
    print "after sort:"
    print a

