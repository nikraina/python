__author__ = 'nikhil'

from threading import Thread
import time

def timer(name,delay,repeat):
    print "Timer " + name + " started"
    while repeat>0:
        time.sleep(delay)
        print name + " : " +str(time.ctime(time.time()))
        repeat -= 1

def driver():
    t1 = Thread(target=timer, args=("Thread 1",2,4))
    t2 = Thread(target=timer, args=("Thread 2",2,4))

    t1.start()
    t2.start()

driver()
print "Main program ended"