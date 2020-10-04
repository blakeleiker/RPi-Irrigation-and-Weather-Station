'''
Class to control a 24 Watt water pump.
24 W + 110 V = 
'''

import time
from hardware import hardware

class WaterPump:

    def __init__(self):
        pass


    def timed_pump(self, t):
        self.start_pump()
        time.sleep(t)
        self.stop_pump()


    def start_pump(self):
        pass


    def stop_pump(self):
        pass

if __name__ == "__main__":
    # Test out the water pump class.

    wp = WaterPump()
    wp.timed_pump(5)