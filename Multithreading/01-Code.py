import threading


def job_1():
    print("This is Job_1")
    for i in range(10000):
        for j in range(10000):
            k = i + j
    print("Job_1 completed")


def job_2():
    print("This is Job_2")
    for i in range(100):
        for j in range(100):
            k = i + j
    print("Job_2 completed")


t1 = threading.Thread(target=job_1)
t2 = threading.Thread(target=job_2)

# Daemon Thread
t1.setDaemon(True)
t1.start()
t2.start()

# job_1()
# job_2()

'''
import threading
threading.current_thread()

Thread Lifecycle
- new
- start -> run()
- runnable
- wait
- dead
'''
