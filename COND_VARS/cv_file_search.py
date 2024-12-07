import os
import time
from threading import Thread, Lock
from wait_group import Wait_Group

mutex = Lock()
matches = []


def file_search(root, filename, wg):
    print(f"Searching in {root}...")
    for file in os.listdir(root):
        full_path = os.path.join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if os.path.isdir(full_path):
            wg.add(1)
            t = Thread(target=file_search, args=(full_path, filename, wg))
            t.start()
    wg.done()


def main():
    wg = Wait_Group()
    wg.add(1)
    start = time.time()
    t = Thread(target=file_search,
               args=("/Users/picsartacademy/Documents", "fsearch_single.py",
                     wg))
    t.start()
    wg.wait()

    end = time.time()
    print(f"\nFINISHED : {end-start:.4f}s\n")
    for m in matches:
        print("\nMatched: ", m)


if __name__ == "__main__":
    main()
