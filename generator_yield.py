__author__ = 'nikhil'

def fib():
    fir = 1
    sec = 1
    while(True):
        yield fir
        fir,sec = sec, fir+sec

def print_fib():
    count = 0
    for num in fib():
        print num
        count += 1
        if(count > 10):
            break


def Main():
    print_fib()

if __name__ == "__main__":
    Main()