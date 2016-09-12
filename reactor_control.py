"""
Checks for heartbeat messages sent to connRecv
Prints error if no beat revied for more than 4 seconds
connRecv: Connection
"""
import multiprocessing

from multiprocessing import freeze_support

import time

import cooling_pump
import steam_generator
from control_rod import CriticalProcess


connR, connS = multiprocessing.Pipe()


def monitor_hb(conn_recv):
    still_going = True
    while still_going:
        if conn_recv.poll(4):
            cooling_pump.pump_water()
            print(conn_recv.recv())
            steam_generator.generate_energy()

        else:
            print('Human input is needed to perform maintenance tasks')
            still_going = False

    print('Reactor shutting down')

if __name__ == '__main__':
    freeze_support()
    crit_proc = CriticalProcess(connS)
    print('Reactor is starting up')
    crit_proc.start()
    monitor_hb(connR)
