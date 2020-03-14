from car import Car
from race import Race
import json


class TestClass:

    #  test if speed is calculated and changed
    def test_speed_correct(self):
        car = Car(1, lambda: None)
        car.update(1584017287,(51.0,-8.4000))
        car.update(1584017314,(51.0,-8.4003))
        assert car.speed != 0
        assert len(car.speed_info) == 2

#  test if bad input 
    def test_speed_bad(self):
        car = Car(1, lambda: None)
        car.update(1584017287,(51.0,-8.4000))
        assert car.speed == 0
        assert len(car.speed_info) == 1


    def test_position_bad(self):
        race = Race(lambda: None)

        car_0 = {
            "timestamp": 1541693114862,
            "carIndex": 0,
            "location": {
            "lat": 51.349937311969725,
            "long": -0.544958142167281
            }
        }


        car_00 = {
            "timestamp": 1541693114887,
            "carIndex": 0,
            "location": {
            "lat": 51.349937311969725,
            "long": -0.544958142167292
            }
        }
        race.update_info(car_0)
        race.update_info(car_00)
        assert race.cars[0].position == 1

    def test_curr_pos(self):
        race = Race(lambda: None)

        car_0 = {
            "timestamp": 1541693114862,
            "carIndex": 0,
            "location": {
            "lat": 51.349937311969725,
            "long": -0.544958142167281
            }
        }

        car_1 = {
            "timestamp": 1541693114862,
            "carIndex": 1,
            "location": {
            "lat": 51.349937311969725,
            "long": -0.544958142167281
            }
        }

        car_2 = {
            "timestamp": 1541693114862,
            "carIndex": 2,
            "location": {
            "lat": 51.349937311969725,
            "long": -0.544958142167281
            }
        }


        car_00 = {
            "timestamp": 1541693114887,
            "carIndex": 0,
            "location": {
            "lat": 51.349937311969725,
            "long": -0.544958142167292
            }
        }

        car_10 = {
            "timestamp": 1541693114887,
            "carIndex": 1,
            "location": {
            "lat": 51.349937311969725,
            "long": -0.544958142167285
            }
        }

        car_20 = {
            "timestamp": 1541693114887,
            "carIndex": 2,
            "location": {
            "lat": 51.349937311969725,
            "long": -0.544958142167296
            }
        }

        race.update_info(car_0)
        race.update_info(car_1)
        race.update_info(car_2)
        race.update_info(car_00)
        race.update_info(car_10)
        race.update_info(car_20)


        assert race.cars[0].position == 2
        assert race.cars[1].position == 3
        assert race.cars[2].position == 1
