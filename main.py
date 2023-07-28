import time
from proxyList import proxyListFormFile
from proxyAuth import authProxyTool
from proxyList import proxyListFromUrl
import threading

#获取列表
# proxyLists = proxyListFormFile.getProxyList()
proxyLists=proxyListFromUrl.getProxyList()


# threadLock = threading.Lock()
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, delay):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.delay = delay
#     def run(self):
#         print ("开启线程： " + self.name)
#         # 获取锁，用于线程同步
#         threadLock.acquire()
#         templist= proxyLists.pop()
#         # 释放锁，开启下一个线程
#         threadLock.release()
#         print(templist.getProxy())
#         if authProxyTool.auth(templist):
#             print(templist.getProxy() + "::::::::" + str(templist.getelseInfo()))
#
#
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
# thread3 = myThread(1, "Thread-1", 1)
# thread4 = myThread(2, "Thread-2", 2)


for list in proxyLists:
    print("start:::::"+list.getProxy())
    if authProxyTool.auth(list):
        print(list.getProxy() + "::::::::" + str(list.getelseInfo()))
