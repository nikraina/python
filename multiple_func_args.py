__author__ = 'nikhil'


def foo(fir, sec, third):
    print "normal exec"
    print fir
    print sec
    print third

# def foo(fir, sec, third, *therest):
#     print "the version with variable params"
#     print fir
#     print sec
#     print third
#     print therest

def foo(fir,sec,third, **options):
    print fir
    print sec
    print third
    if options.get("sum") == True:
        print "sum :: " + str(fir+sec+third)
    if options.get("first") == True:
        print "first element is :: " + str(fir)


foo(1,2,3)
# foo(1,2,3,4,5,6,7)
foo(1,2,3,sum=True)
foo(1,2,3,sum=True,first=True)