from threading import Thread, Condition


class Wait_Group:
    wait_count = 0
    cv = Condition()

    def add(self, num):
        self.cv.acquire()
        self.wait_count += num
        self.cv.release()

    def wait(self):
        self.cv.acquire()
        while self.wait_count > 0:
            self.cv.wait()
        self.cv.release()

    def done(self):
        self.cv.acquire()
        if self.wait_count > 0:
            self.wait_count -= 1
        if self.wait_count == 0:
            self.cv.notify_all()
        self.cv.release()
