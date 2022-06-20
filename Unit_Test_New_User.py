import unittest
import Fair_Billing

class UnitTest(unittest.TestCase):

    def setUp(self):
        self.new_user = "alice"
        self.existing_user = "bob"
        self.data = {"bob": {"session": 4, "seconds": 120}}
        self.stack = {"bob": ["14:55:22"]}
        self.result_data = {"bob": {"session": 4, "seconds": 120}, "alice": {"session": 0, "seconds": 0}}
        self.result_stack ={"bob": ["14:55:22"], "alice": []}

    def test_new_user(self):
        self.assertEqual(Fair_Billing.new_user(self.new_user, self.stack, self.data),(self.result_data, self.result_stack))

    def test_existing_user(self):
        self.assertEqual(Fair_Billing.new_user(self.existing_user, self.stack, self.data),(self.data, self.stack))

if __name__ == "__main__":
    unittest.main()
