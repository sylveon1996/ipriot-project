from sensor import Sensor
from display import Display
from pathlib import Path


class CarPark:
    def __init__(self,
                 location,
                 capacity,
                 log_file='log.txt',
                 plates=None,
                 sensors=None,
                 displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = Path(log_file)
        if not self.log_file.exists():
            self.log_file.touch()

    @property
    def available_bays(self):
        return max(0, self.capacity - len(self.plates))

    def __str__(self):
        return f'Welcome to {self.location} car park'

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Invalid component type")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)

    def remove_car(self, plate):
        self.plates.remove(plate)

    def update_display(self):
        for display in self.displays:
            display.update({"Bays": self.available_bays,
                            "Temperature": 42,
                            })
            print(f"Updating: {display}")
