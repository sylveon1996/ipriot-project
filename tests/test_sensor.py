import unittest
from sensor import Sensor, EntrySensor, ExitSensor
from car_park import CarPark


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor(1, self.car_park, False)
        self.exit_sensor = ExitSensor(1, self.car_park, False)

    def test_entry_sensor_init(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.is_active, False)
        self.assertIsInstance(self.car_park, CarPark)


    def test_vehicles_entry(self):
        self.entry_sensor.update_car_park(plate="ABC123")
        self.entry_sensor.update_car_park(plate="ABC12323")

        self.assertEqual(self.car_park.available_bays, 98)

    def test_vehicles_exit(self):
        self.entry_sensor.update_car_park(plate="ABC123")
        self.entry_sensor.update_car_park(plate="ABC12323")
        self.exit_sensor.update_car_park(plate="ABC12323")


        self.assertEqual(self.car_park.available_bays, 99)

    def test_detect_vehicle(self):
        self.entry_sensor.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, 99)



if __name__ == '__main__':
    unittest.main()













