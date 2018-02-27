"""
Control pixel ring on ReSpeaker 4 Mic Array

pip install pixel_ring gpiozero
"""

import time

from pixel_ring import pixel_ring
from gpiozero import LED

power = LED(5)
power.on()

pixel_ring.set_brightness(10)

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

power.off()
