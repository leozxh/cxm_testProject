from common.myunit import StartEnd
from businessView.loginView import LoginView
import unittest
import logging


class LoginTest(StartEnd):
    csv_file = '../data/account.csv'


    def test_loginlogout_linshiguhang(self):
        logging.info('==========test_login_linshiguhang========')
        l=LoginView(self.driver)
        data = l.get_csv_data(self.csv_file,1)

        l.login_action(data[0],data[1])
        #l.logout_action()

if __name__ == '__main__':
    unittest.main()
