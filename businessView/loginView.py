import logging
from common.cxm_desired_caps import desired_caps
from common.elementlibrary import Login
import time

class LoginView(Login):

    def login_action(self,username,password):
        logging.info('============check_chaiBtn==============')
        self.check_chaiBtn()
        logging.info('============check_Login==============')
        self.check_Login()
        logging.info('============login_action==============')
        logging.info('username is:%s' % username)
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('password is:%s' % password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        time.sleep(6)
        logging.info('click chaiBtn')
        self.check_chaiBtn()
        self.getScreenShot('login finished')
        logging.info('login finished')


    def logout_action(self):
        logging.info('=========logout_action==========')
        logging.info('go to personal center')
        self.driver.implicitly_wait(10)
        self.driver.find_elements(*self.personalCenter)[5].click()
        logging.info('click logoutBtn')
        self.driver.find_element(*self.logoutBtn).click()
        logging.info('click confirmBtn')
        self.driver.find_element(*self.confirmBtn).click()
        self.getScreenShot('logout finished')
        logging.info('logout finished')

if __name__ == '__main__':
    driver=desired_caps()
    # l=LoginView(driver)
    # l.login_action('19000032420','123456')
    # l.logout_action()
