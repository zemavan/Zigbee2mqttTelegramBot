import paho.mqtt.client as mqtt
import json
import os
from dotenv import load_dotenv


load_dotenv()
logFilePath = os.getenv('logFilePath2')


TopicTwo="zigbee2mqtt/fridge"
nameOfTopic="fridge"
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print("error")
    else:
        print("Connected")
        client.subscribe(TopicTwo)

DataType="temperature"
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    broker_in = json.loads(payload)

    data = broker_in[DataType]
    print(data)
    
    with open(logFilePath, 'w')as f:
        f.write(f"The " + DataType + " is " + str(data)+ " from " + nameOfTopic)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("192.168.122.1", 1884, 60)

mqttc.loop_forever()