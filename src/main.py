from car_park import CarPark
from sensor import ExitSensor, EntrySensor
from display import Display


car_park = CarPark("moondalup", 100, log_file="moondalup.txt")
entry = EntrySensor(1, car_park, True)
exits = ExitSensor(2, car_park, True)
display = Display(1, car_park, "Welcome to Moondalup", True)


car_park.register(display)
car_park.register(entry)
car_park.register(exits)


entry.detect_vehicle()
entry.detect_vehicle()
entry.detect_vehicle()
entry.detect_vehicle()
entry.detect_vehicle()
entry.detect_vehicle()
entry.detect_vehicle()
entry.detect_vehicle()
entry.detect_vehicle()
entry.detect_vehicle()
exits.detect_vehicle()
exits.detect_vehicle()


