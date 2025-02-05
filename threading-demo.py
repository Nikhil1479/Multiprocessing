import time
import threading

start = time.perf_counter()


def do_something():
    print("Sleeping for 1 seconds")
    time.sleep(1)
    print("Done Sleeping")


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()
finish = time.perf_counter()
print(f"Program executed in {round(finish - start, 2)} seconds(s)")
