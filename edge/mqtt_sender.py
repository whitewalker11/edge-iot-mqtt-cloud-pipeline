
import time
import json
import paho.mqtt.client as mqtt
import random

with open("config.json") as f:
    config = json.load(f)

BROKER = config["broker"]
PORT = config["port"]
TOPIC = config["topic"]
DEVICE_ID = config["device_id"]

def generate_payload():
    return json.dumps({
        "device_id": DEVICE_ID,
        "temperature": round(random.uniform(25.0, 35.0), 2),
        "humidity": round(random.uniform(40.0, 60.0), 2)
    })

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print(f"Sending messages to MQTT Broker at {BROKER}:{PORT}")
while True:
    payload = generate_payload()
    client.publish(TOPIC, payload)
    print(f"Published: {payload}")
    time.sleep(5)
