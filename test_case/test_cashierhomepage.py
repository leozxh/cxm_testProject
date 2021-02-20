from common.myunit import StartEnd
from businessView.cashierhomepageView import CashierhomepageView
import unittest
import logging

class Cashierhomepage(StartEnd):

    def test_cashierhomepage_linshiguhang(self):
        logging.info('==========test_cashierhomepage_linshiguhang========')
        l=CashierhomepageView(self.driver)
        l.homepage()


if __name__ == '__main__':
    unittest.main()
