import threading
import time

def thread_func(name,id):
    print(f"Thread {name} {id} starting..")
    time.sleep(2)
    print(f"Thread {name} finished..")


if __name__ == "__main__":
    thread1 = threading.Thread(target=thread_func ,args = (2,6))
    thread2 = threading.Thread(target=thread_func ,args = (1,5))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("All threads are finished...")
