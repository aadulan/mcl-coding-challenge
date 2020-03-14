from typing import Dict, Tuple, List
from car import Car

class Race:
    def __init__(self):
        self.cars: Dict[int, Car] = {}
        # self.positions: Dict[int: Car] = {}
        # self.update: bool = False
    
    def update_info(self, data):
        car_i = data["carIndex"]
        if car_i not in self.cars.keys():
            c = Car(car_i)
            self.cars[car_i] = c

        coords = (data["location"]["lat"], data["location"]["long"])
        self.cars[car_i].update(data["timestamp"], coords)

        self.update_positions()

    def update_positions(self):
        # try:
            # pos = [(c.index, c.dist_travel) for c in self.cars.values()]
        sorted_pos = sorted(self.cars.values(), key=lambda x: x.dist_travel, reverse=True)
        print(sorted_pos)
        for i, car in enumerate(sorted_pos):
            car.position = i+1
        # except Exception as e:
        #     print(e)


    



            
        