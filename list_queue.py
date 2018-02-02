class Queue(object):

    def __init__(self):
        self.__list=[]

    def enqueue(self,item):
        self.__list.append(item)


    #判断是出队多还是入队多，尾部添加的话，是入队比较多
    def dequeue(self):
        return self.__list.pop(0)

    def is_empty(self):
        return self.__list==[]

    def size(self):
        return len(self.__list)