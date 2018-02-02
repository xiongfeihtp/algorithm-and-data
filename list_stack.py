#新建一个栈
#压栈push
#出栈pop
#peek查看栈顶元素，不弹出
#非空检测
#返回栈元素的数量

#通过list来实现
class Stack(object):
    def __init__(self):
        self.__list=[]

    def push(self,item):
        #顺序表在尾部操作时间复杂度低，
        #如果使用链表的话，在头部操作比较好。
        self.__list.append(item)

    def pop(self):
        self.__list.pop()

    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None
    def is_empty(self):
        return self.__list==[]

    def size(self):
        return len(self.__list)


if __name__=="__main__":
    s=Stack()