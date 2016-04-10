__author__ = 'nikhil'


def profile(name, *stats):      # *before variable makes it a tuple
    print name
    print stats

profile("python",[2.7,63,(42,44),32],22)

def profile(name, **stats):     # *before variable makes it a dictionary
    print name
    print stats

profile("python", version=2.7, age = 3, tup = (3,6))