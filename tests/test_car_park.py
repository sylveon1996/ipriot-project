import unittest
from car_park import CarPark
from pathlib import Path


class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.new_carpark = CarPark("123 Example Street", 100)

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, Path('log.txt'))

    # ... inside the TestCarPark class
    def test_log_file_created(self):
        self.new_carpark = CarPark("123 Example Street", 100, log_file="new_log.txt")
        self.assertTrue(Path("new_log.txt").exists())

    # ... inside the TestCarPark class
    def tearDown(self):
        Path("new_log.txt").unlink(missing_ok=True)

    def test_logging_of_cars(self):
        self.car_park.add_car("NEW-01")
        with self.car_park.log_file.open("r") as file:
            last_write = file.readlines()[-1]
        self.assertIn("NEW-01", last_write)

    def test_logging_of_car_exit(self):
        self.car_park.add_car("NEW-01")
        self.car_park.remove_car("NEW-01")
        with self.car_park.log_file.open("r") as file:
            last_write= file.readlines()[-1]
        self.assertIn("NEW-01", last_write)
        self.assertIn("exited", last_write)


    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        # Overfilling the car park should not change the number of available bays
        self.assertEqual(self.car_park.available_bays, 0)

        # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register(self):
        with self.assertRaises(TypeError):
            self.car_park.register("Not a Sensor or Display")


if __name__ == "__main__":
    unittest.main()
