class Sensor:
    def __init__(self,
                 id,
                 car_park,
                 is_active=False):

        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"The {self.id} sensor {'is active' if self.is_active else 'not active'}"


class EntrySensor(Sensor):
    ...


class ExitSensor(Sensor):
    ...
