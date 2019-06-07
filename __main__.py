# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:29:45 2019

@author: jfoll
"""

import signal
import time


class GracefulTermination:
    term_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.term_now = True


if __name__ == '__main__':
    graceterm = GracefulTermination()
    while(True):
        print("Doing something in a loop ...")
        time.sleep(1)
        # See if a shutdown is called
        if(graceterm.term_now):
            break

    print('End of the program. I was terminated gracefully.')
