#!/usr/bin/python

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")

'''Sample Output
Starting Thread-1
Starting Thread-2
Exiting Main Thread
Thread-1: Fri Dec 11 23:24:28 2015
Thread-2: Fri Dec 11 23:24:30 2015
Thread-1: Fri Dec 11 23:24:30 2015
Thread-1: Fri Dec 11 23:24:32 2015
Exiting Thread-1
Thread-2: Fri Dec 11 23:24:34 2015
Thread-2: Fri Dec 11 23:24:38 2015
Thread-2: Fri Dec 11 23:24:42 2015
Exiting Thread-2
'''
