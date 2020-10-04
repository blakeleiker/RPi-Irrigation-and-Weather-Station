"""
Define a class which acts as a hardware controller wrapper for the raspberry pi.

Written by Blake Leiker
September 2020 - Initial version
"""

try:
    # Try to import pigpio. Remember to enable pigpiod!
    import pigpio
    TEST_MODE = False
except:
    #print("INITIALIZING TEST MODE")
    TEST_MODE = True

class hardware:


    def __init__(self):
        if TEST_MODE:
            print(f"Initializing hardware in test mode.")
            self.pi = None
        else:
            self.pi = pigpio.pi()


    def enable_output_pin(self, pin_no, name=""):
        if TEST_MODE:
            print(f"Enabling pin {pin_no}.")
        else:
            self.pi.set_mode(pin_no, pigpio.OUTPUT)
            self.pi.write(pin_no, 0)


    def enable_input_pin(self, pin_no, name=""):
        if TEST_MODE:
            print(f"Enabling pin {pin_no}.")
        else:
            self.pi.set_mode(pin_no, pigpio.INPUT)
            

    def disable_pin(self, pin_no):
        if TEST_MODE:
            print(f"Disabling pin {pin_no}.")
        else:
            pass



if __name__ == "__main__":
    # Do a quick test of the hardware class.
    hw = hardware()
    hw.enable_input_pin(1)
    hw.disable_pin(1)