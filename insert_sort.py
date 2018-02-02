def select_sort(alist):
    insert=1
#insert和前面的元素进行比较
    N=len(alist)

    #代表外层循环，取数取了多少次
    for i in range(1,N):
        #内层循环，表示数据正确插入的过程
        while i>0:
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
                i-=1
            #优化算法部分
            else:
                break


