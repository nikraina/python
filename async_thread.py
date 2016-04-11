__author__ = 'nikhil'
import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self,text,out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, "a")
        f.write(self.text + "\n")
        f.close()
        time.sleep(2)
        print "Finished Background write to " + self.out


text = raw_input("Enter the string to store: ")
back = AsyncWrite(text,"out.txt")
back.start()
print "The program is responsive even while the background is writing to a file"

back.join()
print "Now the background thread is also over!!"