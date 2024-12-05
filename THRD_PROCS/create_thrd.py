import time
from threading import Thread


def do_work(id: int):
    print(f"Starting Job: {id}")
    time.sleep(1)
    print(f"Finished Job : {id}")


for i in range(5):
    thrd = Thread(target=do_work, args=(i, ))
    thrd.start()
