import threading

# Global variable
data = None


class threadTwo(threading.Thread):
    def run(self):
        global data
        print 'ran'
        print "Waiting"

        import time
        while True:
            print data
            time.sleep(10) # Delay for 1 minute (60 seconds).


threadTwo().start()
