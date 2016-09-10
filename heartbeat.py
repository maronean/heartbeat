"""

"""

from multiprocessing import Process, freeze_support
from threading import Thread
import multiprocessing
import time

class CriticalThread(Thread):
    def criticalFunctionality(b,a):
    #generic process, will crash with / zero
        return (400 / (20 - a))
        
        
    def run(self):
    #run critical thread until crash
        variable = 0
        while True:
            result = self.criticalFunctionality(variable)
            print("Critical Functions")
            time.sleep(1)
            variable = variable + 1 


            
class CriticalProcess(Process):
    """
    Sends heartbeats to monitoring process
    Extension of Thread Class
    """    
    def __init__(self,connS):
    #dThread = Critical thread to check before sending beat
    #conn sending end of piper for monitoring process
        Process.__init__(self)
        self.conn = connS
    def run(self):
        dThread = CriticalThread()
        dThread.start()
        stillGoing = True
        
        while stillGoing:
            time.sleep(2)
            #send heartbeat if critical thread is still active
            if dThread.is_alive():
                self.conn.send('beat')
                
            else:
            #Thread is dead close the connection
                self.conn.close()
                stillGoing = False
 
"""
Checks for heartbeat messages sent to connRecv 
Prints error if no beat revied for more than 4 seconds
connRecv: Connection
""" 
def monitorHB(connRecv):

    stillGoing = True
    while(stillGoing):
        if connRecv.poll(4):
            print(connRecv.recv())
        
        else:
            print('ERROR')
            stillGoing = False
    print('goodbye')

connR, connS = multiprocessing.Pipe()            
   
if __name__ == '__main__':
    freeze_support()
    critProc = CriticalProcess(connS) 
    critProc.start()        
    monitorHB(connR)

    