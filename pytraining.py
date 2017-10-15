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

#猴子吃桃
l = []
n = 1
for i in range(1,10):
    n = (n+1)*2
    l.append(n)
print (n,l)
    
#打印出如下图案（菱形）:
#第一种方法 
for i in range(4):
    print((3-i)*' '+(2*i+1)*'*')
for i in range(3):
    print((i+1)*' '+(5-2*i)*'*')
#第二种方法
n = int(input("请输入行数 n："))
for i in range(0,n):
    a = abs(i - int(n/2))
    b = n - abs(i - int(n/2))
    print(" "*a+"*"*(b-a))    
#第三种方法
n = int(input("请输入行数 n："))
for i in range(0,n):
    a = abs(i-int(n/2))
    b = n-2*a
    print (a*' '+b*'*')

    
#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
n = int(input('请输入第几项：'))
print ('')
a = 2
b = 1
sum = 0
l = []
for i in range(0,n):
    sum+=((a/b))
    l.append((a/b))
    t = a
    a = a+b
    b = t
      
print ('前%d项之和为%f' % (n,sum))
print (l)
    

#例25 求1+2!+3!+...+20!的和
n = int(input('输入一个数字：'))
l = []
for i in range(1,n+1):
    S = 1
    for j in range(1,i+1):
        S = S*j
    l.append(int(S))
    
sum(l)

#例26 求n!
#方法一
n = int(input('输入一个数字：'))
S = 1
for i in range(1,n+1):
    S = S*i
print (S)
#方法二
def f(n):
    sum = 0
    if n == 0:
        sum = 1
    else :
        sum = n*f(n-1)
        
    return sum 

#例27 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
a = input('请输入一个字符：')
for i in range(1,int(len(a))+1):
    print (a[-i])

#例28 
def f(n):
    Age_n = 10
    for i in range(0,n-1):
        Age_n +=2
    return Age_n

# 例29 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
def y(n):
    global Num
    try:
        Num = int(input('请输入一个不多于5位的正整数：'))
    except ValueError:
        print ('Warning：请输入一个整数！！！')
        y(n)
y(1)        

def f(n):
    global Num
    if len(str(Num))>5:
        print ('Warning!!!输入整数长度有问题，请重新输入！')
        Num = int(input('输入的整数为：'))
        f(n)
    else :
        a = len(str(Num))
        print ('它是%d位数' % a)
        print ('逆序打印出各位数字:',end = '')
        for i in range(1,a+1):
            print (str(Num)[-i],end = ',')        
f(1)

#例30 输入一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
n = input('输入一个整数：')
for i in range(1,int((len(n)/2))+1):
    a = 0
    if n[i-1] == n[-i]:
        a = 1
if a == 1 :
    print ('%d是一个回文数' % int(n))
else :
    print ('%d不是一个回文数' % int(n))

#例33 按逗号分隔列表。
L = [1,2,3,4,5]
s = ','.join(str(n) for n in L)
print (s)

#例35 定义字体颜色
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#例36 求100以内的所有素数（质数）
lower = int(input('输入区间最小值：'))
upper = int(input('输入区间最大值：'))
for num in range(lower,upper):
    if num>1:
        for i in range(2,int(num/2)):
            if num % i == 0:
                break
        else:#如果for循环未被break终止，则执行else块中的语句
            print (num)

#例38 求一个3*3矩阵对角线元素之和
a = []
sum = 0
for i in range(3):
    a.append([])
    for j in range(3):
        n = float((input('请输入一个数：')))
        a[i].append(n)
    sum +=a[i][i]
print (sum)

    
#例39 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中
l = [1,2,3,4,5,6,7]
l.append(int(input('请输入一个数字')))

if l[1]>l[-2]:
    l.sort(reverse=True)
else:
    l.sort()
#例41 静态变量
def varfunc():
    var = 0
    print ('var = %d' % var)
    var += 1
if __name__ == '__main__':
    for i in range(3):
        varfunc()
#作为类的属性    
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar+=1
        print (self.StaticVar)
        
print (Static.StaticVar)

a = Static()
for i in range(3):
    a.varfunc()

#例44 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵
X = [[12,7,3],
    [4,5,6],
    [7,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
l =[]
for i in range(3):
    l.append([])
    for j in range(3):
        l[i].append(X[i][j]+Y[i][j])
print (l)

#例45 统计1--100之和
import datetime
min = int(input('输入最小的一个数\n'))
max = int(input('输入最大的一个数\n'))
sum = 0
begin = datetime.datetime.now()
for i in range(min,max+1):
    sum+=i
print (sum)
end = datetime.datetime.now()
print (end-begin)

#例46 求输入数字的平方，如果平方运算后小于 50 则退出。
Num = int(input('请输入一个数：'))
def f(n):
    print(n**2)

while Num**2<50:
    f(Num)
    Num = int(input('请继续输入一个数：'))
else :
    f(Num)
    
#例47 两个变量值互换
a = int(input("请输入a变量的值: "))
b = int(input("请输入b变量的值: "))
c = a
a = b
b = c
print ('a = %d,b = %d' % (a,b))



