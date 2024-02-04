import time 
from threading import Thread

def job1():
    print("Job1 working ...")
    # simulates cpu consuming
    time.sleep(2)
    print("Job1 done ...")

def job2():
    print("Job2 working ...")
    # simulates cpu consuming
    time.sleep(2)
    print("Job2 done ...")


# less efficient
#job1()
#job2()

# far more efficient
t1 = Thread(target = job1)
t1.start()
t2 = Thread(target = job2)
t2.start()
