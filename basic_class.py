__author__ = 'nikhil'


class sampleClass:
    name = ""
    age = 0
    def printInfo(self):
        print "printing from class method"
        print self.name
        print self.age

obj = sampleClass()
print obj.age
obj.name = "python"
obj.age = 22
obj.printInfo()