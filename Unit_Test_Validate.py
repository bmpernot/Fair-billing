import unittest
import Fair_Billing

class UnitTest(unittest.TestCase):

    def setUp(self):
        self.line1 = "14:55:22 alice Start"
        self.line2 = "14:55:22 alice End"
        self.line3 = "14:56:22 alice"
        self.line4 = "14:56:22 End"
        self.line5 = "alice Start"
        self.result_positive = True
        self.result_negative = False

    def test_validate1(self):
        self.assertEqual(Fair_Billing.validate(self.line1), self.result_positive)

    def test_validate2(self):
        self.assertEqual(Fair_Billing.validate(self.line2), self.result_positive)
        
    def test_validate3(self):
        self.assertEqual(Fair_Billing.validate(self.line3), self.result_negative)
        
    def test_validate4(self):
        self.assertEqual(Fair_Billing.validate(self.line4), self.result_negative)
        
    def test_validate5(self):
        self.assertEqual(Fair_Billing.validate(self.line5), self.result_negative)

if __name__ == "__main__":
    unittest.main()
