from common.myunit import StartEnd
from businessView.repaymentView import RepaymentView
import unittest
import logging

class RepaymentTest(StartEnd):

    def test_repayment_linshiguhang(self):
        logging.info('==========test_repayment_linshiguhang========')
        l=RepaymentView(self.driver)
        l.credit()
        l.partialpayment()
        l.repayment()


if __name__ == '__main__':
    unittest.main()