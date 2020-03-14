import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import json
from race import Race

print(f"starting...")

race = Race()

print(f"created race object: {race}")

def on_message(client, userdata, message):
    data = json.loads(message.payload)
    race.update_info(data)
    print("%s" % (data))


def main():
    client = mqtt.Client("v1")
    client.connect("broker",port=1883)
    client.subscribe("carCoordinates")
    client.on_message = on_message
    client.loop_forever()

# def publish_event():


# subscribe.callback(on_message, "carCoordinates", hostname="broker")
if __name__ == '__main__':
    print("hello world")
    main()