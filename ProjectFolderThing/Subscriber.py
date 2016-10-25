from mosquitto import *
from serial import *
from random import *
SPEED = 115200

# FULL DEVICE NAME can be found by running: python PortScanner.py
# SPEED is usually 115200 for Microbit and 9600 for Arduino
board = Serial("/dev/cu.usbmodem14412",SPEED,timeout=2)

randomID = random()
client = Mosquitto("LightSubscriber" + str(randomID))
client.connect("10.212.61.136")

# The rest of your code goes in here !!!
client.subscribe("/lights")

def messageReceived(broker, obj, msg):
    global client
    payload = msg.payload.decode()
    print("Message " + msg.topic + " containing: " + payload)
    if (payload == "ON"):
        send = "1"
    else:
        send = "0"
    board.write(send.encode())
    
client.on_message = messageReceived

while (client != None): client.loop()

