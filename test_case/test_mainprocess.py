from common.myunit import StartEnd
from businessView.mainprocessView import MainProcessView
import unittest
import logging

class MainprocessTest(StartEnd):

    def test_mainprocess_linshiguhang(self):
        logging.info('==========test_addgoods_linshiguhang========')
        l=MainProcessView(self.driver)
        l.goodsInventory()
        l.addBatch()
        l.salesOrder()

if __name__ == '__main__':
    unittest.main()
