"""
Checks for heartbeat messages sent to connRecv
Prints error if no beat revied for more than 4 seconds
connRecv: Connection
"""
import multiprocessing

from multiprocessing import freeze_support

import cooling_pump
import steam_generator
from control_rod import CriticalProcess


mainConnR, mainConnS = multiprocessing.Pipe()
backupConnR, backupConnS = multiprocessing.Pipe()


def monitor_hb(conn_recv):
    still_going = True
    while still_going:
        if conn_recv.poll(4):
            #print(conn_recv.recv())
        else:
            print('Processed Stopped')
            still_going = False

if __name__ == '__main__':
    freeze_support()
    crit_proc = CriticalProcess('Critical', mainConnS)
    back_up_crit_proc = CriticalProcess('Back up', backupConnS, True)
    print('Reactor is starting up')
    crit_proc.start()
    back_up_crit_proc.start()
    monitor_hb(mainConnR)
    print('Critical Process Failure, Switching to backup process')
    monitor_hb(backupConnR)

    print('Done')
