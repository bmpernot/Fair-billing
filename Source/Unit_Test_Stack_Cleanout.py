import unittest
import Fair_Billing

class UnitTest(unittest.TestCase):

    def setUp(self):
        self.data = {"alice" : {"session": 2, "seconds": 60}, "bob": {"session": 4, "seconds": 120}}
        self.stack = {"alice": ["14:55:22"], "bob": ["14:56:22", "14:57:22"]}
        self.end_time = "14:58:22"
        self.time_format = "%H:%M:%S"
        self.results = {"alice" : {"session": 3, "seconds": 240}, "bob": {"session": 6, "seconds": 300}}

    def test_stack_cleanout(self):
        self.assertEqual(Fair_Billing.stack_cleanout(self.stack, self.end_time, self.data, self.time_format),self.results)

if __name__ == "__main__":
    unittest.main()
