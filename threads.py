#!/usr/bin/python

import threading
import time
import random

exitFlag = False

gyro_value = 0
compass_value = 0

gyroLock = threading.Lock()
compassLock = threading.Lock()


class gyroThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Starting gyroThread")

        while (True):

            if exitFlag:
                exit()

            time.sleep(1)
            gyroLock.acquire()
            # time.sleep(1)
            global gyro_value
            gyro_value = random.randint(0, 5)
            print("setting gyro value to {}".format(gyro_value))
            gyroLock.release()


class compassThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Starting compassThread")

        while (True):

            if exitFlag:
                exit()

            time.sleep(1)
            compassLock.acquire()
            # time.sleep(1)
            global compass_value
            compass_value = random.randint(0, 5)
            print("setting compass value to {}".format(compass_value))
            compassLock.release()


gt = gyroThread()
ct = compassThread()

gt.start()
ct.start()

try:
    while threading.active_count() > 0:
        print("Main thread: reading values")

        compassLock.acquire()
        c = compass_value
        compassLock.release()

        gyroLock.acquire()
        g = gyro_value
        gyroLock.release()

        # time.sleep(3)
        print("Main thread: gyro value={}, compass value={}".format(g, c))
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Ctrl-c received! Sending kill to threads...")
    exitFlag = True
