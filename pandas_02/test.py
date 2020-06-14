import pddb
import unittest

class TestPdata(unittest.TestCase):
    """Tester for the function patients_with_missing_values in
    treatment_functions.
    """

    def get_data(self):
        expected = 6593
        x = pddb.get_data()
        actual = len(x)
        self.assertEqual(expected, actual)


    def get_time_series(self):
        df = pddb.get_time_series()
        print(df['interval'])

if __name__ == '__main__':
    unittest.main(exit=False)