from common.myunit import StartEnd
from businessView.codelistcenterView import CodelistcenterView
import unittest
import logging

class Codelistcenter(StartEnd):

    def test_codelistcenter_linshiguhang(self):
        logging.info('==========test_codelistcenter_linshiguhang========')
        l=CodelistcenterView(self.driver)
        l.codelistcenter()


if __name__ == '__main__':
    unittest.main()