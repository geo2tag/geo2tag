from threading import Thread
import time


def in_thread(self, _):
    for i in range(1, 5):
        print 'sec' + str(i)
        time.sleep(1)
    self.thread.join()


class thread_start():

    def start(self):
        self.thread = Thread(target=in_thread, args=(self, None))
        self.thread.start()

thread_start().start()
