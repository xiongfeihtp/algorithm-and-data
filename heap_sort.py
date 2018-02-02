#堆调整
import random
def heapify(alist,HeapSize,root):
    left=2*root
    right=2*root+1
    larger=root
    if left<HeapSize and alist[larger]<alist[left]:
        larger=left
    if right<HeapSize and alist[larger]<alist[right]:
        larger=right
    if larger!=root:
        alist[root],alist[larger]=alist[larger],alist[root]
        heapify(alist,HeapSize,larger)


#创建堆,最大堆
def build_heap(alist):
    N=len(alist)
    for i in range((N-2)//2,-1,-1): #对所有的非叶节点进行调整
        heapify(alist,N,i)

def heap_sort(alist):
    build_heap(alist)
    N=len(alist)
    for i in range(N-1,-1,-1):
        alist[0],alist[i]=alist[i],alist[0]
        heapify(alist,i,0)

if __name__=="__main__":
    a=[random.randint(1,1000) for i in range(1000)]
    print(a)
    heap_sort(a)
    print(a)
