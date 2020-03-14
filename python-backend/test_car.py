from car import Car

class TestClass:
    def test_speed_correct(self):
        car = Car(1)
        # car.speed_info.append((1584017287,(51.0,-8.4000)))
        # car.speed_info.append((1584017314,(51.0,-8.4003)))
        car.update(1584017287,(51.0,-8.4000))
        car.update(1584017314,(51.0,-8.4003))
        assert car.speed != 0

    def test_speed_bad(self):
        car = Car(1)
        # car.speed_info[1584017287] = (51.0,-8.4000)
        car.update(1584017287,(51.0,-8.4000))
        assert car.speed == 0

    

    # def test_two(self):
    #     x = "hello"
    #     assert hasattr(x, "check")