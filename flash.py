from machine import Pin
import time
import neopixel

pin = machine.Pin("LED", machine.Pin.OUT)
pixel = machine.Pin(5, machine.Pin.OUT)

pixel1 = neopixel.NeoPixel(pixel, 50)

while True:
    pin.on()
    pixel1[1] = (100, 0, 0)
    pixel1.write()
    time.sleep_ms(100)
    pin.off()
    pixel1[1] = (0, 0, 0)
    pixel1.write()
    time.sleep(.5)
