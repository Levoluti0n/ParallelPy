import os
import time
from threading import Thread, Lock

mutex = Lock()
matches = []


def file_search(root, filename):
    print(f"Searching in {root}...")
    childs = []
    for file in os.listdir(root):
        full_path = os.path.join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if os.path.isdir(full_path):
            t = Thread(target=file_search, args=(full_path, filename))
            t.start()
            childs.append(t)
    for ch in childs:
        ch.join()


def main():
    start = time.time()
    t = Thread(target=file_search,
               args=("/Users/picsartacademy/Documents", "fsearch_single.py"))
    t.start()
    t.join()
    end = time.time()
    print(f"\nFINISHED : {end-start:.4f}s\n")
    for m in matches:
        print("\nMatched: ", m)


main()
