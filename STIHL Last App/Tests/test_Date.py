import unittest
from Domain.Date import Date


class TestDate(unittest.TestCase):

    def test_str__valid_input__correct_conversion_to_string(self):
        # Case 1
        date = Date(5, 6, 2000)
        self.assertTrue(date.__str__(), "05-06-2000")
        # Case 2
        date = Date(15, 6, 2000)
        self.assertTrue(date.__str__(), "15-06-2000")
        # Case 3
        date = Date(5, 11, 2000)
        self.assertTrue(date.__str__(), "05-11-2000")
        # Case 4
        date = Date(24, 11, 2000)
        self.assertTrue(date.__str__(), "24-11-2000")

    def test_string_to_date__valid_input__correct_conversion_to_date(self):
        date_string = "05-06-2000"
        date = Date.string_to_date(date_string)
        self.assertEqual(date.day, 5)
        self.assertEqual(date.month, 6)
        self.assertEqual(date.year, 2000)

    def test_generate_current_date__valid_input__current_date_returned_as_Date_object(self):
        date = Date.generate_current_date()
        date.day = 4
        self.assertEqual(date.day, 4)

    
if __name__ == '__main__':
    unittest.main()
