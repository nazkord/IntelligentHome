from mainUI import Pilot
from threading import Thread
import mqtt.subscriber as subscriber
from time import sleep

root = Pilot()

thread = Thread(target = subscriber.run, args = (root.rooms, ))
thread.start()
sleep(3)	#waiting for subscriber to initialize

root.mainloop()