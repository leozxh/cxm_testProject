from  baseView.baseView import BaseView
from common.cxm_desired_caps import desired_caps
from selenium.common.exceptions import NoSuchElementException
import logging.config
from selenium.webdriver.common.by import By
import os
import time
import csv
from common.keycode import InputMethod
from faker import Faker
import random
from common.random_goods import random_cai
from common.mysqlverification import *




class Common(BaseView):

    #取消无拆包单位弹框
    cancel_chaiBnt=(By.ID,'com.zhiyi.cxm.caixm_prep:id/confirm_button')
    #检查打印机无纸弹框
    outofPaper = (By.ID,'woyou.aidlservice.jiuiv5:id/textView_btn')
    #检查有输入框不输入数值是出现的弹框
    confirmButton = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/confirm_button')
    # 下单按钮
    cashierchoosedopenOrder = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/cashier_choosed_open_order')
    # 左侧相同tab
    personalCenter = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tab_textview')
    # 退出登录
    logoutBtn = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/btn_login_out')
    # 确定按钮
    confirmBtn = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/confirm_button')

    def check_Login(self):
        try:
            element = self.driver.find_element(*self.cashierchoosedopenOrder)
        except NoSuchElementException:
            logging.info('Not logged in')
        else:
            logging.info('Already logged in')
            logging.info('go to personal center')
            self.driver.implicitly_wait(10)
            self.driver.find_elements(*self.personalCenter)[5].click()
            logging.info('click logoutBtn')
            self.driver.find_element(*self.logoutBtn).click()
            logging.info('click confirmBtn')
            self.driver.find_element(*self.confirmBtn).click()
            logging.info('logout finished')



    def check_chaiBtn(self):
        try:
            element = self.driver.find_element(*self.cancel_chaiBnt)
        except NoSuchElementException:
            logging.info('chai element is not found!')
        else:
            logging.info('click cancelBtn')
            element.click()

    def check_paper(self):
        try:
            element = self.driver.find_element(*self.outofPaper)
        except NoSuchElementException:
            logging.info('outofPaper element is not found!')
        else:
            logging.info('============Out of Paper============')
            element.click()

    def check_confirmBtn(self):
        try:
            element = self.driver.find_element(*self.confirmButton)
        except NoSuchElementException:
            logging.info('confirmButton element is not found!')
        else:
            logging.info('click confirmButton')
            element.click()




    def get_screenSize(self):
        '''
        获取屏幕尺寸
        :return:
        '''
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return (x, y)

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_screenSize()
        y1 = int(l[1] * 0.5)
        x1 = int(l[0] * 0.95)
        x2 = int(l[0] * 0.25)
        self.swipe(x1, y1, x2, y1, 1000)

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self, csv_file, line):
        '''
        获取csv文件指定行的数据
        :param csv_file: csv文件路径
        :param line: 数据行数
        :return:
        '''
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    def enableAppiumUnicodeIME(self):
        InputMethod().enableAppiumUnicodeIME()  # 切换回appium输入法


    def fakename(self):
       fake = Faker(locale='zh_CN')
       fake_name = fake.name()+str(random.randint(1, 999))
       return fake_name

    def fakephone(self):
       fake = Faker(locale='zh_CN')
       fake_phone = fake.phone_number()
       return fake_phone

    def randomproduct(self):
        random_product = random_cai()
        return random_product

    def checkaddcustomer(self):
        checkaddcustomer=check_add_customer(self)
        return checkaddcustomer


    if __name__ == '__main__':
        driver = desired_caps()

