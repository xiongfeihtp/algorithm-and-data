# node object
#特殊情况，空链表和只有一个节点,头节点，尾节点

#在不知道对象怎么实现的时候，可以先去想想怎么使用，在去编写对象。面向对象的结构化设计。
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

#在编写对象的时候，考虑各种极限情况
class singleLinkedList(object):
    # 链表中的操作，对象方法，方法的功能和输入
    # 链表的属性，对象属性,私有性

    #默认参数，None保证，没有节点输入的时候，创造一个空链表
    def __init__(self,node=None):
        self.__head=node
        if node:
            node.next=node
    def is_empty(self):
        #判断头节点是否为空就性
        if self.__head==None:
            return True
        else:
            return False

    def length(self):
        #返回节点数目，从节点遍历到尾节点，遍历的时候需要有一个游标Cur
        # 需要一个游标,循环，并且判断最后的一个位置
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1  #循环单向链表只能为1
        while cur.next!= self.__head: #循环单向链表只能为这个条件
            count += 1
            cur = cur.next
        return count
         #游标移动


    def travel(self):
        cur=self.__head
        while cur.next!=self.__head:
            print(cur.elem) #打印不换行
            cur=cur.next
    #退出循环的时候，尾节点没有打印
        print(cur.next)


    def add(self, item): #头插入
        node=Node(item)
        if self.is_empty():
            self.__head=node
            node.next=node
            return True


        cur=self.__head
        while cur.next != self.__head:
            print(cur.elem)  # 打印不换行
            cur = cur.next
        node.next = self.__head
        # 需要遍历一次
        self.__head = node
        cur.next=node


    def append(self, item):
        node=Node(item)
        cur=self.__head
        #判断当前的链表是否为空链表
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            while cur.next!=self.__head:
                cur=cur.next
            node.next=self.__head
            cur.next=node

    def insert(self, pos, item):
        #游标 pos从0开始的
        node=Node(item)
        if pos<0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)

        else:
            cur=self.__head
            for i in range(pos-1):
                cur=cur.next
            node.next=cur.next
            cur.next=node


    def remove(self, item):
#先搜索,再删除,两个辅助游标,空链表不执行任何操作
        cur=self.__head
        pre=None
        if self.is_empty():
            return False
        while cur.next!=self.__head:#cur走动最后,但是遍历的时候，最后一个节点没有遍历到
            if cur.elem==item:
                #先判断是不是头结点
                if cur==self.__head:
                    #头节点,先找到尾部节点
                    rear=self.__head
                    while rear.next!=self.__head:
                        rear=rear.nexy
                    self.__head=cur.next
                    rear.next=self.next
                #只有头结点的时候，才涉及到找到尾节点
                    return True
                else:
                    #中间节点
                    pre.next=cur.next
                    return True
            else:
                pre=cur
                cur=cur.next
        #尾节点判断
        if cur.elem==item:
            if cur==self.__head:
             #链表当中只有一个节点
                self.__head=None
                return True
            else:
                pre.next=cur.next
                return True
        return False


    def search(self,item):#单链表的两种结束方式
        cur=self.__head
        count=0
        if self.__head==None:
            return False

        while cur.next!=self.__head:
            if cur.elem!=item:
                cur=cur.next
                count+=1
            else:
                return count
        if cur.elem==item:
            return (count+1)
        return False

#测试
if __name__=="__main__":
    Link=singleLinkedList(3)