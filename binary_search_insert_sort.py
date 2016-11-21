#!/usr/bin/python
#--*-- coding:utf-8 --*--

def binary_search_insert_sort(a):
    for index in range(1, len(a)):
        tmp = a[index]
        left = 0
        right = index -1
        #binary search
        while left <= right:
            mid = (left + right) /2 
            if a[mid] > tmp:
                right = mid -1
            else:
                left = mid +1

        #move
        if left != index:
            del a[index]
            a.insert(left, tmp)

if __name__ == "__main__":
    a = [12, 21, 1, 42, 14, 42, 56,21]
    print "before sort:"
    print a
    binary_search_insert_sort(a)
    print "after sort:"
    print a

