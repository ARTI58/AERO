import time
from rpi_ws281x import *

LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 120     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

#jast one
strip.setPixelColor(0,  Color(150, 150, 150))
strip.show()
time.sleep(5)

#step to step
i = 0
while i < 30:
        strip.setPixelColor(i,  Color(0, 100, 0))
        strip.show()
        time.sleep(0.2)
        i = i+1
#led off 
i = 0
while i < 30:
        strip.setPixelColor(i,  Color(0, 0, 0))
        strip.show()
        time.sleep(0.2)
        i = i+1
#on all
i = 0
while i < 30:
        strip.setPixelColor(i,  Color(120, 0, 0))
        i = i+1
strip.show()
time.sleep(2)


#off all
i = 0
while i < 30:
        strip.setPixelColor(i,  Color(0, 0, 0))
        i = i+1
strip.show()
