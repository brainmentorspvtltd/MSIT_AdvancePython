import threading


def job():
    print(f"Job started by {threading.current_thread().getName()}")
    for i in range(100):
        for j in range(2000):
            k = i + j
    print(f"Job completed by {threading.current_thread().getName()}")


for i in range(5):
    t = threading.Thread(target=job, name=f"Thread_{i}")
    t.start()
