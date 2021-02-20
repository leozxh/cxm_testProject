import logging
from common.cxm_desired_caps import desired_caps
from common.elementlibrary import Codelistcenter

class CodelistcenterView(Codelistcenter):

    def codelistcenter(self):
        logging.info('============Click chaiBtn============')
        self.check_chaiBtn()
        logging.info('============Jump Code List Center============')
        self.driver.find_element(*self.tvrightButton).click()

if __name__ == '__main__':
    driver=desired_caps()