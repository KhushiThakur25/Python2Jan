import threading 

def square(n):
    print(f"Square : {n*n}")

def cube(n):
    print(f"cube : {n*n*n}")
    

if __name__ == "__main__":
    t1 = threading.Thread(target = square,args=(10,))
    t2 = threading.Thread(target= cube,args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All threads are finished...")