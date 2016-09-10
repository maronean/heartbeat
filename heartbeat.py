"""

"""

from multiprocessing import Process, freeze_support
from threading import Thread
import multiprocessing

class CriticalThread(Thread):
    def run(self):
        while True:
            a = 2
            

            
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
        #send heartbeat if critical thread is still active
        while stillGoing:
            if dThread.is_alive():
                self.conn.send(['beat'])
            else:
                self.conn.send('dead')
                self.conn.close()
                stillGoing = False
                
def monitorHB(connRecv):
    stillGoing = True
    while(stillGoing):
        print('hello')
        try:
            print('yes')
            print(connRecv.recv())
            print('hello')
            
            sleep(2)
        except:
            print('ERROR')
            stillGoing = false
        print('goodbye')

connR, connS = multiprocessing.Pipe()            
   
if __name__ == '__main__':
    freeze_support()
    critProc = CriticalProcess(connS) 
    critProc.start()        
monitorHB(connR)

    