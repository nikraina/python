__author__ = 'nikhil'

class Parent:
    def get_name(self):
        print "I am parent"

    def get_info(self):
        print "I am created using Python"

class Child(Parent):
    def get_name(self):
        print "I am child"



def Main():
    obj = Child()
    obj.get_name()
    obj.get_info()


if __name__ == "__main__":
    Main()
