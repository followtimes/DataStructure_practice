#!/usr/bin/env python
#--*-- coding:utf-8 --*--

#主要是做有序数组的合并，考虑只有一个数组，则即利用下标将一个数组当做两个来排序，注意排序完后填入原数组的对应下标
#剩下的就是将整个乱序数组,使用递归来做乱序数组的从1到2到4的依次合并


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
