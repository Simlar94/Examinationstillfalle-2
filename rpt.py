from gpiozero import MotionSensor
from datetime import datetime
from picamera import PiCamera
import time

camera = PiCamera()
pir = MotionSensor(4)
while True:
	pir.wait_for_motion()
	camera.resolution = (1024, 768)
	filename = ("bild.jpeg")
	camera.hflip = True
	camera.vflip = True
	camera.capture(filename)
	time.sleep(2)
