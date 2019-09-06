#!/usr/bin/python
#--*-- coding:utf-8 --*--

#选定最左边为基准，将比基准大的都放到基准右边，比基准小的都放到基准左边，然后递归操作基准左边的数组，基准右边的数组

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

