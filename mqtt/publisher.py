import paho.mqtt.client as broker
port = 1883
broker_address = "127.0.0.1"


class Publisher:

    def __init__(self):
        self.client = broker.Client("publisher1")
        self.client.connect(broker_address, port, 60)


    def publish(self, topic, payload):
    	print("PUBLISHER: send message %s on topic %s" %(payload, topic))
    	result = self.client.publish(topic, payload)
    	if result[1] > 10:
    		self = Publisher()
    		self.client.publish(topic, payload)