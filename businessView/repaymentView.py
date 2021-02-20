'''
说明：
选择买家-整单赊欠/部分付款-还款
'''
import logging
from common.cxm_desired_caps import desired_caps
from common.elementlibrary import Repayment
import time

class RepaymentView(Repayment):

    def  credit(self):
        # logging.info('============Check Paper============')
        # self.check_paper()
        time.sleep(10)
        logging.info('============Click chaiBtn============')
        self.check_chaiBtn()
        logging.info('============Choose batch ==============')
        self.driver.find_elements(*self.tvTitle)[1].click()
        logging.info('============Choose Product ==============')
        self.driver.find_elements(*self.saleNametv)[0].click()
        logging.info('============Choose quantity==============')
        self.driver.find_elements(*self.layoutextfeeContainer )[0].click()
        logging.info('============Input quantity==============')
        self.driver.find_elements(*self.btnNumber)[4].click()
        logging.info('===========Determine===============')
        self.driver.find_element(*self.tvCommit).click()
        logging.info('===========Show user===============')
        self.driver.find_element(*self.showUser).click()
        logging.info('===========Select user===============')
        self.driver.find_elements(*self.tvTitle)[9].click()
        logging.info('===========Sales Order===============')
        self.driver.find_element(*self.cashierchoosedopenOrder).click()
        logging.info('===========Whole bill===============')
        self.driver.find_element(*self.tvfinanceCredit).click()

    def partialpayment(self):
        # logging.info('============Click chaiBtn============')
        # self.check_chaiBtn()
        # logging.info('============Choose batch ==============')
        # self.driver.find_elements(*self.tvTitle)[1].click()
        logging.info('============Choose Product ==============')
        self.driver.find_elements(*self.saleNametv)[0].click()
        logging.info('============Choose quantity==============')
        self.driver.find_elements(*self.layoutextfeeContainer)[0].click()
        logging.info('============Input quantity==============')
        self.driver.find_elements(*self.btnNumber)[4].click()
        logging.info('===========Determine===============')
        self.driver.find_element(*self.tvCommit).click()
        logging.info('===========Show user===============')
        self.driver.find_element(*self.showUser).click()
        logging.info('===========Select user===============')
        self.driver.find_elements(*self.tvTitle)[9].click()
        logging.info('===========Sales Order===============')
        self.driver.find_element(*self.cashierchoosedopenOrder).click()
        logging.info('============Input quantity==============')
        self.driver.find_elements(*self.btnNumber)[4].click()
        logging.info('============Cash register==============')
        self.driver.find_element(*self.btncheckOut).click()

    def repayment(self):
        # logging.info('============Click chaiBtn============')
        # self.check_chaiBtn()
        logging.info('============Jump to Buyer Center============')
        self.driver.find_elements(*self.sameBtn)[1].click()
        self.driver.implicitly_wait(10)
        logging.info('============Click Order management============')
        self.driver.find_elements(*self.tvtabTitle)[1].click()
        logging.info('============Choose Order============')
        self.driver.find_elements(*self.tvView)[0].click()
        logging.info('============Click Repay============')
        self.driver.find_element(*self.btnbillRepay).click()
        logging.info('============Click btnrepayOrder============')
        self.driver.find_element(*self.btnrepayOrder).click()
        logging.info('============Repay finished!============')

if __name__ == '__main__':
    driver=desired_caps()