from typing import Dict, Tuple, List
from geopy.distance import geodesic
from car_status_type import Status
import json

class Car:
    def __init__(self, index: int, publish_callback):
        self.index: int = index
        self.speed: float = 0
        self.position: int = 0
        self.speed_info: List[Tuple[float, Tuple[float, float]]] = []
        # calculate postition from distance travelled
        self.dist_travel: float = 0
        self.publish_callback = publish_callback
        self.count: int = 0

    def calc_speed(self, dist, delta_t):
        #  calculate speed km/hr
        return dist/(delta_t/3600)

    def calc_dist(self, latlng1, latlng2):
        #  calculates geodesic distance from two coordinates
         return geodesic(latlng1, latlng2)
        
    def update(self, timestamp, coord):
        #  updates car with new info 

        self.speed_info.append((timestamp,coord))

        # must have at least 2 items
        l = self.speed_info[-2:]
        if len(l) < 2 :
            self.speed = 0
            self.dist_travel = 0
            return 
    
        position_1, poistion_2 = l
        
        t1, latlng1 = position_1
        t2, latlng2 = poistion_2
        
        
        dist = self.calc_dist(latlng1, latlng2)
        self.dist_travel += dist.km

        #  divide time by 1000 to get seconds from milliseconds
        delta_t = (t2 - t1)/1000
        speed = self.calc_speed(dist, delta_t)

        #  turn speed into mph
        self.speed: float = speed.miles
        self.count+=1
        
        #  only publish event if all the cars have updated once
        if self.count % 5 == 0:
            self.count = 0
            self.car_status_json(Status.POSITION, self.position)
            self.car_status_json(Status.SPEED, self.speed)

        # try:
        # except Exception as e:
        #     print(e)

    def car_status_json(self, status, val):
        # creates json to publish event
        
        # {
        #     "timestamp": 1541693114862,
        #     "carIndex": 2,
        #     "type": "POSITION",
        #     "value": 1
        #  }

        d = {
            "timestamp": self.speed_info[-1][0] ,
            "carIndex": self.index,
            "type": status.name,
            "value": val 
        }
        self.publish_callback("carStatus", d)
        # print(event)

    def __repr__(self):
        return f"<Car {self.index}, pos={self.position}, speed={round(self.speed, 2)}, dist={round(self.dist_travel,4)}>"
    
