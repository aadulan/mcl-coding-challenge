# MAT Fan Engagement Coding Challenge

## Prerequisites:

* [docker](https://docs.docker.com/)
* [docker-compose](https://docs.docker.com/compose/)

## Run Code

<pre><code>$ docker-compose pull
$ docker-compose up -d
</code></pre>

## Run Tests

<pre><code>$ pytest
</code></pre>

## Notes

- Classes:
  - Race
  - Car
- The client susbcribes to the `carCoordinates` topic
- The race class updates all the cars
- If the car does not exist, a car is created and then updated
- Car Position is determined by calculating total distance travelled 
- The speed (mph) is calculated by using two consectuive `carCoordinate` updates. The distance is calculated by using the `geodesic` function which takes in two coordinates.
- Race class exposes a callback to the car class which publishes messages to the MQTT Client.
- Every time all the cars are updates, the speed and position of each car is published
- An event is published by tracking car positions and calculating which car has overtaken

## Assumptions
- All cars are following a racing line so I can calculate position by using total distance travelled
- No cars will be going in reverse 
- All cars start at the same location 

-------------------------------------------------


## Introduction

The purpose of this challenge is for you to demonstrate
* write and structure a simple backend application in an appropriate language of your choice
* parse and transform streamed telemetry data
* deliver a component to integrate into a stack of technologies

Feel free to use any libraries, frameworks or dependencies you want in order to achieve the task.

Please include instructions on how to build and run your code, any tests you've written and some text explaining what you did.

If you are already familiar with the underlying technologies we hope that it won't take you more than a couple of hours to get your application up and running.

## Scenario

Real-time data from a Formula 1 race has been recorded and streamed into our system. We want to use that data in order to increase fan engagement by providing a live visualisation.

## Challenge

Raw telemetry data is arriving via MQTT. A basic front-end application has been developed to visualise F1 cars going around a track. It can also display an event stream and car status information such as speed and position, but currently it is not receiving this information.

Please develop a data processing application which subscribes to the provided MQTT broker and consumes data from the following MQTT topic with the format shown:

* **carCoordinates**

    ```console
      {
        timestamp: number,
        carIndex: number,
        location: {
          lat: float,
          long: float
         }
      }
    ```

  e.g.

    ```json
      {
        "timestamp": 1541693114862,
        "carIndex": 2,
        "location": {
          "lat": 51.349937311969725,
          "long": -0.544958142167281
         }
      }
    ```

It should then publish aggregated and enriched data on the following MQTT topics using the format described:

- **carStatus**

    ```console
      {
        timestamp: number,
        carIndex: number,
        type: string<SPEED|POSITION>,
        value: number
      }
    ```

  e.g.

    ```json
      {
        "timestamp": 1541693114862,
        "carIndex": 2,
        "type": "POSITION",
        "value": 1
      }
    ```

- **events**

    ```console
      {
        timestamp: number,
        text: string
      }
    ```

  e.g.

    ```json
      {
        "timestamp": 1541693114862,
        "text": "Car 2 races ahead of Car 4 in a dramatic overtake."
      }
    ```

All these topics will then be forwarded via a gateway-like MQTT-to-WebSocket service to the frontend application.

## Architecture

![Components](./components.svg)

## Getting started

Start all components:

```console
$ docker-compose pull
$ docker-compose up -d
Creating network "mat-coding-challenge_default" with the default driver
Creating broker ... done
Creating source_gps        ... done
Creating mqtt-to-websocket ... done
Creating webapp            ... done
```

Open (http://localhost:8084)

Test the setup with `mosquitto_pub` or a similar MQTT client:

```console
$ mosquitto_pub -t events -f examples/event.json
$ mosquitto_pub -t carStatus -f examples/position.json
$ mosquitto_pub -t carStatus -f examples/speed.json
```

You should now see a car's position and an event in the webapp.
