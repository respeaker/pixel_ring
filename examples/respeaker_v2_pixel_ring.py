"""
Control pixel ring on ReSpeaker V2

sudo apt install python-mraa libmraa1
pip install pixel-ring

"""

import time

from pixel_ring import pixel_ring
import mraa
import os

en = mraa.Gpio(12)
if os.geteuid() != 0 :
    time.sleep(1)
 
en.dir(mraa.DIR_OUT)
en.write(0)

pixel_ring.set_brightness(20)

if __name__ == '__main__':
    while True:

        try:
            pixel_ring.wakeup()
            time.sleep(3)
            pixel_ring.think()
            time.sleep(3)
            pixel_ring.speak()
            time.sleep(6)
            pixel_ring.off()
            time.sleep(3)
        except KeyboardInterrupt:
            break


    pixel_ring.off()
    time.sleep(1)

en.write(1)
