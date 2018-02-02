from timeit import Timer
"""
def test1():
    ls=[]
    for i in range(10000):
        ls.append(i)
def test2():
    ls=[]
    for i in range(10000):
        ls=ls+[i]
#生成器
def test3():
    ls=[i for i in range(10000)]

def test4():
    ls=list(range(10000))

timer1=Timer('test1()','from __main__ import test1')
print('test1:',timer1.timeit(1000))

timer2=Timer('test2()','from __main__ import test2')
print('test2:',timer2.timeit(1000))

timer3=Timer('test3()','from __main__ import test3')
print('test3:',timer3.timeit(1000))

timer4=Timer('test4()','from __main__ import test4')
print('test4:',timer4.timeit(1000))
"""

def t6():
    ls=[]
    for i in range(10000):
        ls.append(i)
def t7():
    ls=[]
    for i in range(10000):
        ls.insert(0,i)
timer6=Timer('t6()','from __main__ import t6')
print('test7:',timer6.timeit(1000))

timer7=Timer('t7()','from __main__ import t7')
print('test8:',timer7.timeit(1000))