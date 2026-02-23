import paho.mqtt.client as mqtt
import json
from dotenv import load_dotenv

load_dotenv()
logFilePath = os.getenv('logFilePath')

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected")
    client.subscribe("zigbee2mqtt/tester")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    broker_in = json.loads(payload)

    if "temperature" in broker_in:
        temp = broker_in["temperature"]
        print("Temperature now is", temp)
        logs_in = temp
        
        with open (logFilePath, 'w') as f:
            f.write(f"The temperature is " + str(logs_in))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect("192.168.122.1", 1884, 60)
mqttc.loop_forever()
