import pddb
import unittest

class TestPdata(unittest.TestCase):
    """Tester for the function patients_with_missing_values in
    treatment_functions.
    """

    def setUp(self):
        self.db = pddb.PDDB()

    def test_top_female_ratings(self):
        """测试根据女性观众的top电影，按照F列降序排序"""

        top_female_ratings = self.db.top_female_ratings()
        print(top_female_ratings[:10])

    def test_get_diff(self):
        """测试按照diff排序产生评分差异最大的电影"""

        sorted_by_diff = self.db.sorted_by_diff()
        print(sorted_by_diff[:10])
        # 男性喜欢但是女性评分不高的电影
        print(sorted_by_diff[::-1][:10])

if __name__ == '__main__':
    unittest.main(exit=False)