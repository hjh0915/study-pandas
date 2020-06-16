import pddb
import unittest

class TestPdata(unittest.TestCase):
    """Tester for the function patients_with_missing_values in
    treatment_functions.
    """

    def setUp(self):
        self.db = pddb.PDDB()

    def test_rating_std_by_title(self):
        """测试通过评分的方差来计算出最大异议的电影"""

        rating_std_by_title = self.db.rating_std_by_title()
        print(rating_std_by_title.sort_values(ascending=False)[:10])

if __name__ == '__main__':
    unittest.main(exit=False)