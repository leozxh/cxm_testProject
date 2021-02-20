from appium import webdriver
import logging.config
import yaml
import os
from os import path
#CON_LOG = '../config/log.config'
log_file_path = path.join(path.dirname(path.abspath(__file__)), '../config/log.conf')
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()

def desired_caps():

    with open('../config/cxm_caps.yaml', 'r',encoding='utf-8') as file:
         data = yaml.load(file, Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['Version'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['unicodeKeyboard'] =data['unicodeKeyboard'] #使用unicodeKeyboard的编码方式来发送字符串
    desired_caps['resetKeyboard'] =data['resetKeyboard'] #将键盘隐藏
    #desired_caps['automationName'] = data['Uiautomator2']

    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appname'])

    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)

    driver.implicitly_wait(10)

    return driver

if __name__ == '__main__':
    desired_caps()