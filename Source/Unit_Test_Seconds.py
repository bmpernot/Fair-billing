import unittest
import Fair_Billing

class UnitTest(unittest.TestCase):

    def setUp(self):
        self.first_time = "14:55:22"
        self.second_time = "14:56:22"
        self.time_format = "%H:%M:%S"
        self.results = 60

    def test_seconds(self):
        self.assertEqual(Fair_Billing.seconds(self.first_time, self.second_time, self.time_format),self.results)

if __name__ == "__main__":
    unittest.main()
