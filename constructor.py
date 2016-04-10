__author__ = 'nikhil'

class sampleClass:
    def __init__(self,name):    #__init__ is the constructor
        print "this is class constructor"
        self.name = name
    def getName(self):
        print self.name

obj = sampleClass("python")
obj.getName()