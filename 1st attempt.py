#Cristmas project - 1st attempt

# import various GPIO devices

from gpiozero import LED
from gpiozero import Button
from gpiozero import DistanceSensor
import time

# setup the devices

led = LED(6)
button = Button(3)

led.off()

sensor = DistanceSensor(echo=17, trigger=4)
while True:
    print('Distance: ', sensor.distance * 100)
    if (sensor.distance*100) <=5:
        led.on()
        print("on")
        time.sleep(1)
    else:
        led.off()
        print("off")
        time.sleep(1)
