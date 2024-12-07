from threading import Thread, Condition
import time


class StingySpendy:
    money = 100
    cv = Condition()

    def stingy(self):
        for i in range(1000000):
            self.cv.acquire()
            self.money += 10
            self.cv.notify()
            self.cv.release()
        print("Stingy Done!")

    def spendy(self):
        for i in range(500000):
            self.cv.acquire()
            while self.money < 20:
                self.cv.wait()
            self.money -= 20
            self.cv.release()
        print("Spendy Done!")


def main():
    ss = StingySpendy()
    Thread(target=ss.stingy, args=()).start()
    Thread(target=ss.spendy, args=()).start()
    time.sleep(2)
    print(f"Total money : {ss.money}")


if __name__ == "__main__":
    main()
