#!/usr/bin/python
#--*-- coding:utf-8 --*--

def quick_sort(a, left, right):
    if left < right:
        key = a[left]
        low = left
        high = right
        while low < high:
            #因为基准数为left，所以先从高处遍历，拿出比基准数小的，放在基准数的左边
            while low < high and a[high] >= key:
                high -= 1
            a[low] = a[high]
            #从低处开始，拿到比基准数大的，放在基准数右边
            while low < high and a[low] < key:
                low += 1
            a[high] = a[low]
        #将基准数放在当前基准位置
        a[low] = key
        #基准数左边的进行上述操作
        quick_sort(a, left, low - 1)
        #基准数右边的进行上述操作
        quick_sort(a, low + 1, right)



if __name__ == "__main__":
    a = [12, 21, 1, 42, 14, 42, 56,21]
    print "before sort:"
    print a
    quick_sort(a, 0, len(a) - 1)
    print "after sort:"
    print a

