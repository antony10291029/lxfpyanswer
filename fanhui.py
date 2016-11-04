# -*- coding: utf-8 -*-
#可变参数求和，可变参数是指args这个参数是任意值，输入多少就就求和
def calc_sum(*args):#参数带星号，代表接受任意多个参数都可以
    ax = 0
    for i in args:
        ax = ax+ i
    return ax
print(calc_sum(9,5,7,3,5,1,8))
#如果不需要立即求和，那就是可以函数嵌套函数
#闭包的意思就是返回一个函数，函数本身就是一种抽象的方式，所以返回的不是结果
#而结果是在被返回的函数中定义的计算方式计算出来的
#由于返回的是抽象计算方式，所以闭包可以重定义返回函数的内部抽象方式，实现不更改调用方法，而修改调用的内容
def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax =ax + i
        return ax
    return sum
print(lazy_sum(9,5,7,3,5,1,8))#打印的是一个函数
f = lazy_sum(9,5,7,3,5,1,9)
h = lazy_sum(9,5,7,3,5,1,9)
print(f)
print(h)
print(f())
print(f == h)
#关于闭包的一个坑
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
(f1)
(f2)
(f3)




