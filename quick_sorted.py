#!/usr/bin/python
#--*-- coding:utf-8 --*--

def quick_sort(a, left, right):
    if left < right:
        key = a[left]
        low = left
        high = right
        while low < high:
            while low < high and a[high] >= key:
                high -= 1
            a[low] = a[high]
            while low < high and a[low] < key:
                low += 1
            a[high] = a[low]
        a[low] = key
        quick_sort(a, left, low - 1)
        quick_sort(a, low + 1, right)



if __name__ == "__main__":
    a = [12, 21, 1, 42, 14, 42, 56,21]
    print "before sort:"
    print a
    quick_sort(a, 0, len(a) - 1)
    print "after sort:"
    print a

