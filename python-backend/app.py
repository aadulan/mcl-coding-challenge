import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import json
from race import Race
from car_status_type import Status

# print(f"starting...")


def main():
    client = mqtt.Client("v1")

    # updates the race everytime a message comes in
    def on_message(client, userdata, message):
        data = json.loads(message.payload)
        race.update_info(data)

    #  callback to publish topics to the broker
    def publish_event(topic, data):
        event = json.dumps(data)
        client.publish(topic, event)

    race = Race(publish_callback=publish_event)

    client.connect("broker",port=1883)
    client.subscribe("carCoordinates")
    client.on_message = on_message
    client.loop_forever()



# def publish_event():


# subscribe.callback(on_message, "carCoordinates", hostname="broker")
if __name__ == '__main__':
    main()