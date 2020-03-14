import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import json
from race import Race
from car_status_type import Status

print(f"starting...")


# print(f"created race object: {race}")


    # print("%s" % (data))


def main():
    client = mqtt.Client("v1")

    def on_message(client, userdata, message):
        data = json.loads(message.payload)
        race.update_info(data)

    def publish_event(topic, data):
        event = json.dumps(data)
        # print(f"published to {topic}: {event}")
        client.publish(topic, event)

    race = Race(publish_callback=publish_event)
    client.connect("broker",port=1883)
    client.subscribe("carCoordinates")
    client.on_message = on_message
    # publish_event()
    client.loop_forever()



# def publish_event():


# subscribe.callback(on_message, "carCoordinates", hostname="broker")
if __name__ == '__main__':
    print("hello world")
    main()