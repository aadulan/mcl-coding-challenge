from typing import Dict, Tuple, List
from geopy.distance import geodesic
import json

class Car:
    def __init__(self, index: int):
        self.index: int = index
        self.speed: float = 0
        self.position: int = 0
        self.speed_info: List[Tuple[float, Tuple[float, float]]] = []
        # calculate postition from distance travelled
        self.dist_travel: float = 0

    def calc_speed(self, dist, delta_t):
        return dist/(delta_t/3600)

    def calc_dist(self, latlng1, latlng2):
         return geodesic(latlng1, latlng2)
        
    def update(self, timestamp, coord):
        
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

        delta_t = (t2 - t1)/1000
        speed = self.calc_speed(dist, delta_t)

        self.speed: float = speed.km
        print("updated")
        # self.car_status_json()

    def car_status_json(self):
        # {
        #     "timestamp": 1541693114862,
        #     "carIndex": 2,
        #     "type": "POSITION",
        #     "value": 1
        #  }
        d = {
            "timestamp": 1541693114862,
            "carIndex": self.index,
            "type": "POSITION",
            "value": self.position
        }

        event = json.dumps(d)
        print(event)

    def __repr__(self):
        return f"<Car {self.index}, pos={self.position}, speed={round(self.speed, 2)}, dist={round(self.dist_travel,4)}>"
    
