import unittest
from common.cxm_desired_caps import desired_caps
import logging
from  time import sleep

class StartEnd(unittest.TestCase):

    def setUp(self):
        logging.info('======setUp=========')
        self.driver=desired_caps()


    def tearDown(self):
        logging.info('======tearDown=====')
        sleep(5)
        self.driver.close_app()