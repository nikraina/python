__author__ = 'nikhil'

def simple():
    print "Hello I am a simple function"


def dec(func):
    def inner():
        print "function extending begins"
        func()
        print "function extending ends"
    return inner

simple = dec(simple)

simple()