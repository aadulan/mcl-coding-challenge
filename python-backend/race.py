from typing import Dict, Tuple, List
from car import Car
from car_status_type import Status
import random

class Race:
    def __init__(self, publish_callback):
        self.cars: Dict[int, Car] = {}
        self.publish_callback = publish_callback
        self.prev_pos: List[Tuple[int, Car]] = []
        # self.update: bool = False
    
    def update_info(self, data):
        car_i = data["carIndex"]
        if car_i not in self.cars.keys():
            c = Car(car_i, self.publish_callback)
            self.cars[car_i] = c

        coords = (data["location"]["lat"], data["location"]["long"])
        self.cars[car_i].update(data["timestamp"], coords)

        self.update_positions()

    def update_positions(self):
        self.prev_pos = self.get_curr_pos()
        # try:
            # pos = [(c.index, c.dist_travel) for c in self.cars.values()]
        sorted_pos = sorted(self.cars.values(), key=lambda x: x.dist_travel, reverse=True)
        # print(sorted_pos)
        for i, car in enumerate(sorted_pos):
            car.position = i+1
            
        try:
            self.get_event()
        except Exception as e:
            print(e)
        # except Exception as e:
        #     print(e)
    def get_curr_pos(self):
        # (car position, car)
        return sorted([(c.position, c) for c in self.cars.values()], key= lambda x: x[1].index)

    def get_event(self):
        curr_pos = self.get_curr_pos()
        combine_pos = zip(self.prev_pos, curr_pos)
        diff_pos = [prev - cur for (prev, _), (cur, _) in combine_pos]
        # print(diff_pos)
        # diffs = [c for a,c in diff_pos if a!=0]

        for car_i, diff in enumerate(diff_pos):
            if diff > 0:
                prev_pos, car = self.prev_pos[car_i]
                loss = [c.index for pos,c in curr_pos if pos == prev_pos][0]

                self.event_json(car, loss)        


    
    def event_json(self, gain, loss):

        msgs = [
            "Car %d overtakes Car %d",
            "Overtake! Car %d goes in front of Car %d",
            "Car %d races ahead of Car %d in a dramatic overtake."
        ]
        d = {
            "timestamp": gain.speed_info[-1][0],
            "text": msgs[random.randint(0, len(msgs)-1)] % (gain.index, loss)
            # f"Car {gain} races ahead of Car {loss} in a dramatic overtake."
         }
        
        self.publish_callback("events", d)



    # def send_car_status():



    



            
        