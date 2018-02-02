def select_sort(alist):
    """选择排序"""
    N=len(alist)
    for j in range(N-1):
        min=j
        for i in range(j+1,N):
            if alist[min]>alist[i]:
                min=i
        #放到一次循环的外部
        alist[j],alist[min]=alist[min],alist[j]
    return alist


if __name__=="__main__":
    li=[5,4,21,5,7,5,5,4,3,2]
    print(li)
    select_sort(li)
    print(li)