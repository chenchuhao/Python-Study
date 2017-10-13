# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:14:39 2017

@author: 15521
"""

# -*- 面向对象编程 -*-
#类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
#类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
#数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
#方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。

#父类
class people:
     #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print ('%s 说:我%d岁' % (self.name,self.age))
#继承        
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
        
    def speak(self):
        print ('%s说：我%d岁了，我在读%d年级了' % (self.name,self.age,self.grade))
        
#多继承
#另一个类，多重继承之前的准备
class speaker:
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
        
    def speak(self):
        print ('我叫%s，是一个演说家，我的演讲主题是：%s' % (self.name,self.topic))
#多重继承
#方法名同，默认调用的是在括号中排前地父类的方法        
class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)        
        
        
        
        
        
        