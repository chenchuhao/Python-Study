# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:57:56 2017

@author: 15521
"""

print ("-----------------华丽丽的分割线------------------")
x = int(input("FirstInt："))
y = int(input("ScondInt："))
z = int(input("ThirdInt："))

list = [x,y,z]

list.sort()

for i in list:
    print (i)
    
    
#从小到大排序    
l = []
for i in range(3):
    x = int(input("integer:\n"))
    l.append(x)

l.sort()
print (l)

#斐波那契数列
def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

fib(3)


#输出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print ('%d*%d=%d\t' % (i,j,i*j),end = '')
        
        
#暂停一秒输出
import time 
MyD = {1:'a',2:'b'}
for key,value in dict.items(MyD):
    print (key,value)
    time.sleep(1)
    
    
#求兔子数量
b = int(input('月份：'))
def Rab(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

Rab(b)
    

#101-200的素数
for i in range(101,201):
    if i%3 !=0 and i%2!=0 and i%5!=0:
        print (i,end = '  ')

#水仙花数
for n in range(100,1000):
    i = int(n/100)
    j = int(n/10)%10
    k = n%10
    if n == i**3+j**3+k**3:
        print (n)


#分解质因数
def reduceNum(n):
    print ('{} = '.format(n),end = ''),
    if not isinstance(n,int):
        print ('请输入一个正确的数字！')
        exit(0)
    elif n in [1]:
        print ('{}'.format(n))
    while n not in [1]:#n=1时跳出循环
        for index in range(2,n + 1):
            if n % index==0:
                n=int(n/index)#python3除法会自动转化为float
                if n==1:
                    print (index)
                else:
                    print ('{}*'.format(index),end = '')
                break#打破for循环
            
reduceNum(8)

#分数分级
a = int(input('输入分数：\n'))

print ('A' if a>=90 else ('B' if a>=60 else 'C'))


#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
import string
s = input('请输入一个字符：\n')
num = 0
letters = 0
space = 0
digit = 0
others = 0

for i in s:
    if i.isalpha():
        letters+= 1
    elif i.isnumeric():
        num+= 1
    elif i.isspace():
        space+= 1
    elif i.isdigit():
        digit+= 1
    else:
        others+= 1
        
print ('num = %d,char = %d,space = %d,digit = %d,others = %d' % (num,letters,space,digit,others))
        
#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
#例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
n = int(input('n（个数）等于：\n'))
a = int(input('a的值等于：\n'))
Tn = 0
s = []
for i in range(n):
    Tn+= a
    a = a*10
    s.append(int(Tn))
    
print('')    
print(s,Tn)
print ('s = %d' % (sum(s)))


#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数
import datetime
begin = datetime.datetime.now()
for i in range(2,1001):
    l = []
    sum = 0
    for index in range(1,i):
        if i%index == 0:
            l.append(int(index))   
            sum+=index
    if sum == i:
        print (i,l)
        
end = datetime.datetime.now()
print (end-begin)

#自由落体：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

h = 100
sum = 100
n = int(input('第几次落地：\n'))

def f(n):
    global h#引用全局变量时加声明global
    global sum 
    for i in range(1,n+1):
        h = h/2
        sum+=h*2
        if i == n:
            print ('在第%d次落地时，共经过%f米' % (n,sum))
            print ('第%d次反弹有%f米高' % (n,h))
            
f(n)













