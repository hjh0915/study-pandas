import pddb
import unittest

class TestPdata(unittest.TestCase):
    """Tester for the function patients_with_missing_values in
    treatment_functions.
    """

    def setUp(self):
        self.db = pddb.PDDB()

    def test_merge_tables(self):
        """测试关联三张表"""

        data = self.db.merge_tables()
        print(data[:5])

    def test_sex_ratings(self):
        """测试按性别分级每部电影的平均电影评分"""

        sex_ratings = self.db.sex_ratings()
        print(sex_ratings[:5])

    def test_active_titles(self):
        """测试过滤少于250个评分的电影"""

        active_titles = self.db.active_titles()
        print(active_titles)

    def test_get_active_rows(self):
        """测试从mean_ratings中选出评分多于250个的电影信息"""

        mean_ratings = self.db.get_active_rows()
        print(mean_ratings)

if __name__ == '__main__':
    unittest.main(exit=False)