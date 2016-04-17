__author__ = 'nikhil'

def loop_items():
    for n in range(0,10):
        yield n

def count():
    for num in loop_items():
        print num

def Main():
    count()

if __name__ == "__main__":
    Main()