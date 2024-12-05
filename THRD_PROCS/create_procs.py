import time
from multiprocessing import set_start_method, Process


def do_work(id: int):
    print(f"Starting Job: {id}")
    time.sleep(1)
    print(f"Finished Job : {id}")


if __name__ == "__main__":
    set_start_method('spawn')
    for i in range(5):
        p = Process(target=do_work, args=(i, ))
        p.start()
        print(p)
