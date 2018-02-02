def merge_sort(alist):
    """归并排序"""
    # 拆分过程
    N = len(alist)
    if N <= 1:
        return alist   #必须要有返回值，才能保证程序的正常运行
    mid = N // 2
    # 传入的是新的列表，但是将排序好的部分作为返回值
    # left 采用归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid])
    # right 采用归并排序后形成的有序的新的列表
    right_li = merge_sort(alist[mid:])

    # 将两个有序的子序列进行合并
    left_pointer, right_pointer = 0, 0
    result=[]
    while left_pointer<len(left_li) and right_pointer<len(right_li):
        if left_li[left_pointer]<=right_li[right_pointer]:  #=条件，可以保证稳定
            result.append(left_li[left_pointer])
            left_pointer+=1
        else:
            result.append(right_li[right_pointer])
            right_pointer+=1
    #退出循环的时候将剩下的部分也追加到新的列表内
    result+=left_li[left_pointer:]
    result+=right_li[right_pointer:]
    return result

if __name__ == "__main__":
    li = [5, 4, 21, 5, 7, 5, 5, 4, 3, 2]
    print(li)
    sorted_list=merge_sort(li)  #排序好的新列表会以返回值的形式呈现
    print(sorted_list)