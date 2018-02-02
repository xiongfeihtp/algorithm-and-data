def shell_sort(alist):
    """希尔排序"""
    N=len(alist)
    i=1
    gap=N//2 #Python3中取整
#控制gap
    while gap>0:#gap需要取到1
        # 外部的控制,一个循环将所有子序列进行遍历
        #希尔算法，与普通的插入算法的区别就是gap的步长
        for j in range(gap,N):
        #内部子序列控制
            i=j
            while i>0:   #比较和交换
                if alist[i]<alist[i-gap]:
                    alist[i],alist[i-gap]=alist[i-gap],alist[i]
                    i-=gap
                else:
                    break
        gap=gap//2

#希尔排序如何最优

if __name__=="__main__":
    li=[5,4,21,5,7,5,5,4,3,2]
    print(li)
    shell_sort(li)
    print(li)