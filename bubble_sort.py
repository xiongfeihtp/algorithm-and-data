def bubble_sort(alist):
    #顺序表和链表
    """冒泡排序"""
    N=len(alist)
    for j in range(N-1):
        count=0
        for i in range(0,N-1-j):#操作下标交换元素比较方便
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
                count+=1
    #优化，中间某次有序就退出
        if count==0:
            return alist
    return alist


if __name__=="__main__":
    li=[5,4,21,5,7,5,5,4,3,2]
    print(li)
    bubble_sort(li)
    print(li)