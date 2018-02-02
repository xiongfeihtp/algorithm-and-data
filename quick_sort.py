def quick_sort(alist, first, last):
    # 递归的终止条件
    if first >= last:  # 操作的只有一个元素,有可能减1后first比last小
        return
        # N = len(alist)
    mid_value = alist[first]
    Low = first
    High = last
    while Low < High:
        # 开始移动
        # 只要不重合就可以一直走
        # 将相等的值放在一边
        # High
        while Low < High and alist[High] >= mid_value:  # 这里是将相等的值放在High的那边
            High -= 1
        # 不能走时执行交换
        alist[Low] = alist[High]
        # Low+=1 这里注释掉，是为了避免交错

        # Low
        while Low < High and alist[Low] < mid_value:
            Low += 1
        alist[High] = alist[Low]
        #   High-=1
    # 循环退出的时候Low=High
    alist[Low] = mid_value
    # 在原有的序列的标号上面操作，传递的时候不能传递新的列表，直接传递原列表。
    # 对Low左边的列表执行快速排序
    quick_sort(alist, first, Low - 1)
    # 对Low右边的列表执行快速排序
    quick_sort(alist, Low + 1, last)


if __name__ == "__main__":
    li = [5, 4, 21, 5, 7, 5, 5, 4, 3, 2]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
