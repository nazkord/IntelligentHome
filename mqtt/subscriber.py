import paho.mqtt.client as broker
port = 1883
broker_address = "127.0.0.1"


class Subscriber:

    def __init__(self, rooms):
    	self.rooms = rooms   
    	self.client = broker.Client("subscriber1")
    	self.client.on_connect = self.subscribe_all_topics
    	self.client.on_message = self.process_message
    	self.client.connect(broker_address, port, 60)


    def subscribe_all_topics(self, client, userdata, flags, rc):
    	for room in self.rooms.values():
        	for light in room.lighting.values():
        		self.client.subscribe(light.location + "/+") 		# subscribe to all light's config elements (one level wildcard)


    def process_message(self, client, userdata, message):
    	payload = str(message.payload.decode('utf-8'))
    	print("SUBSCRIBER: received message %s on topic %s" %(payload, message.topic))
    	topic = message.topic.split('/')							# example topic: room/bathroom/light/downer/brightness
    	room = self.rooms[topic[1]]
    	light = room.lighting[topic[3]]
    	parameter = topic[4]
    	if parameter == 'power':
    		light.change_power()
    	elif parameter == 'brightness':
    		light.change_brightness(payload)
    	elif parameter == 'color':
    		light.change_color(payload)


def run(rooms):
    sub = Subscriber(rooms)
    sub.client.loop_forever()
