import threading
import time
import logging

# Logging Levels
# CRITICAL -> 5   25
# ERROR -> 4     100
# WARNING -> 3   50
# INFO -> 2    200
# DEBUG -> 1   4500
# NOTSET -> 0

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)s) %(message)s')


def job():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')
    logging.error("Some error found...")


for i in range(3):
    th = threading.Thread(target=job)
    th.start()
