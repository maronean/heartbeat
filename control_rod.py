import random
from multiprocessing import Process

import time
from threading import Thread


class CriticalProcess(Process):
    """
    Sends heartbeats to monitoring process
    Extension of Thread Class
    """

    def __init__(self, connS):
        # dThread = Critical thread to check before sending beat
        # conn sending end of piper for monitoring process
        Process.__init__(self)
        self.conn = connS

    def run(self):
        dThread = CriticalThread()
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
            self.critical_functionality(variable)
            time.sleep(2)


class ControlRodException(Exception):
    def __init__(self, message=None):
        self.message = message
