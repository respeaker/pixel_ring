

from . import usb_pixel_ring_v1
from .apa102_pixel_ring import PixelRing


pixel_ring = usb_pixel_ring_v1.find()
if not pixel_ring:
    pixel_ring = PixelRing()

