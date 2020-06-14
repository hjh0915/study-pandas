import pddb
import unittest

class TestPdata(unittest.TestCase):
    """Tester for the function patients_with_missing_values in
    treatment_functions.
    """

    def test_time_range_dtl(self):
        """测试时间间隔区间交易金额汇总"""

        tran_date = '20191127'
        dr_cr_flag = '2'
        x = pddb.get_time_range_dtl(tran_date, dr_cr_flag)
        for k in x:
            print(k)

if __name__ == '__main__':
    unittest.main(exit=False)