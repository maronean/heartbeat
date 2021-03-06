import random
from multiprocessing import Process

import time
from threading import Thread


class CriticalProcess(Process):
    """
    Sends heartbeats to monitoring process
    Extension of Thread Class
    """

    def __init__(self, thread_name, connS, no_kill=False):
        # dThread = Critical thread to check before sending beat
        # conn sending end of piper for monitoring process
        Process.__init__(self)
        self.thread_name = thread_name
        self.conn = connS
        self.no_kill = no_kill

    def run(self):
        print("Starting " + self.thread_name + " Process")
        dThread = CriticalThread(self.no_kill)
        dThread.start()
        still_going = True

        while still_going:
            time.sleep(2)
            # send heartbeat if critical thread is still active
            if dThread.is_alive():
                self.conn.send('Control Rods are still functioning')

            else:
                # Thread is dead close the connection
                self.conn.close()
                still_going = False



class CriticalThread(Thread):
    initiated = False
    no_kill = False

    def __init__(self, no_kill=False):
        Thread.__init__(self)
        self.no_kill = no_kill

    def critical_functionality(self, a):
        num = random.randint(0, 10)
        if num % 4 == 0 and self.initiated:
            raise ControlRodException('Critical Failure!!!')
        elif not self.initiated:
            self.initiated = True
        return

    def run(self):
        # run critical thread until crash
        variable = 0
        while True:
            if not self.no_kill:
                self.critical_functionality(variable)
            time.sleep(2)


class ControlRodException(Exception):
    def __init__(self, message=None):
        self.message = message
