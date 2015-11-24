# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 06:27:07 2015

@author: Nick
"""

class MyClass(object):
    instance_count = 0
    def __init__(self, value):
        self.__value = value
        MyClass.instance_count += 1
        print "instance No {} created".format(MyClass.instance_count)
        
    def aMethod(self, aValue):
        self.__value *= aValue
    
    def __str__(self):
        return "A MyClass instance with value: " + str(self.__value)
    
    def __del__(self):
        MyClass.instance_count -= 1
        
class SubClass(Parent):
    def __init__(self, aValue):
        super(SubClass, self).__init__(aValue)