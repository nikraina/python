__author__ = 'nikhil'

import threading
import time

tlock = threading.Lock()

def timer(name,delay,repeat):
    print "Timer " + name + " started"
    tlock.acquire()
    while repeat>0:
        time.sleep(delay)
        print name + " : " +str(time.ctime(time.time()))
        repeat -= 1
    print name + " is releasing the lock"
    tlock.release()

def driver():
    t1 = threading.Thread(target=timer, args=("Thread 1",2,4))
    t2 = threading.Thread(target=timer, args=("Thread 2",2,4))

    t1.start()
    t2.start()

driver()
print "Main program ended"