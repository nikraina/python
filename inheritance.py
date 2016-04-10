__author__ = 'nikhil'

class parentClass:
    def setName(self,name):
        self.name = name
    def getName(self):
        print self.name

class childClass(parentClass):
    pass

class childClass2(parentClass):
    def getName(self):
        print "this is child class 2"
        print self.name

obj = childClass()
obj.setName("pycharm")
obj.getName()

obj2 = childClass2()
obj2.setName("pycharm of child class 2")
obj2.getName()