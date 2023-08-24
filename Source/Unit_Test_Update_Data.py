import unittest
import Fair_Billing

class UnitTest(unittest.TestCase):

    def setUp(self):
        self.username = "alice"
        self.seconds = 60
        self.data = {"alice" : {"session": 2, "seconds": 60}, "bob": {"session": 4, "seconds": 120}}
        self.results = {"alice" : {"session": 3, "seconds": 120}, "bob": {"session": 4, "seconds": 120}}

    def test_update_data(self):
        self.assertEqual(Fair_Billing.update_data(self.username, self.seconds, self.data),self.results)

if __name__ == "__main__":
    unittest.main()
