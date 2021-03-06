'''
说明：
主流程：新增货品-新增批次入库-售卖/开码单
'''
import logging
from common.cxm_desired_caps import desired_caps
from common.elementlibrary import Mainprocess



class MainProcessView(Mainprocess):

    def goodsInventory(self):
        logging.info('============Check Paper============')
        #logging.info('============检查纸张============')
        self.check_paper()
        logging.info('============Click chaiBtn============')
        self.check_chaiBtn()
        logging.info('============Go to goods Inventory ==============')
        self.driver.find_elements(*self.sameBtn)[3].click()
        logging.info('============Go to goods Management ==============')
        self.driver.find_elements(*self.goodsManagement)[1].click()
        logging.info('============Click add new goods Btn ==============')
        self.driver.find_element(*self.addNewgoods).click()
        logging.info('============Switch input method============')
        self.enableAppiumUnicodeIME()
        logging.info('============Enter product name ==============')
        self.driver.find_elements(*self.setgoodsName)[0].send_keys(self.randomproduct())
        logging.info('============Enter product specifications ==============')
        self.driver.find_elements(*self.setgoodsName)[1].send_keys(5)
        logging.info('============Enter the sales price ==============')
        self.driver.find_elements(*self.setgoodsName)[2].send_keys(5)
        logging.info('============Click save Btn==============')
        self.driver.find_element(*self.saveBtn).click()
        logging.info('============Add product finished!==============')

    def addBatch(self):
        # logging.info('============Check Paper============')
        # self.check_paper()
        # logging.info('============Click chaiBtn============')
        # self.check_chaiBtn()
        logging.info('============Switch inventory management==============')
        self.driver.find_elements(*self.goodsManagement)[0].click()
        logging.info('============Click addbatch==============')
        self.driver.find_element(*self.addNewbatch).click()
        logging.info('===========Click addshipper===============')
        self.driver.find_element(*self.addShipper).click()
        logging.info('============Switch input method============')
        self.enableAppiumUnicodeIME()
        logging.info('===========Enter shipper===============')
        self.driver.find_element(*self.setgoodsName).send_keys(self.fakename())
        logging.info('============Click save Btn==============')
        self.driver.find_element(*self.saveBtn).click()
        logging.info('===========Next step===============')
        self.driver.find_element(*self.nextStep ).click()
        logging.info('===========Choose product===============')
        self.driver.find_elements(*self.chooseProduct)[0].click()
        logging.info('===========Input quantity===============')
        self.driver.find_elements(*self.btnNumber)[6].click()
        self.driver.find_elements(*self.btnNumber)[9].click()
        self.driver.find_elements(*self.btnNumber)[9].click()
        logging.info('===========Determine===============')
        self.driver.find_element(*self.tvCommit).click()
        logging.info('===========Confirm storage===============')
        self.driver.find_element(*self.tvConfirm).click()

    def salesOrder(self):
        # logging.info('============Check Paper============')
        # self.check_paper()
        # logging.info('============Click chaiBtn============')
        # self.check_chaiBtn()
        logging.info('============Go to Cashier Homepage ==============')
        self.driver.find_elements(*self.sameBtn)[0].click()
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
        # logging.info('===========Confirm===============')
        # self.check_confirmBtn()
        logging.info('===========Sales Order===============')
        self.driver.find_element(*self.cashierchoosedopenOrder).click()
        logging.info('===========Cash register===============')
        self.driver.find_element(*self.btncheckOut).click()
        logging.info('===========Sales Order finised!===============')
        logging.info('============Open code ==============')
        logging.info('============Choose Product ==============')
        self.driver.find_elements(*self.saleNametv)[0].click()
        logging.info('============Choose quantity==============')
        self.driver.find_elements(*self.layoutextfeeContainer)[0].click()
        logging.info('============Input quantity==============')
        self.driver.find_elements(*self.btnNumber)[4].click()
        logging.info('===========Determine===============')
        self.driver.find_element(*self.tvCommit).click()
        # logging.info('===========Confirm===============')
        # self.check_confirmBtn()
        logging.info('============Click Open code==============')
        self.driver.find_element(*self.btnsavesingleCode).click()
        # logging.info('===========Confirm===============')
        # self.check_confirmBtn()



if __name__ == '__main__':
    driver=desired_caps()