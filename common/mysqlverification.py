#查询数据库结果验证
import logging
from selenium.webdriver.common.by import By
from common.mysql_query import MysqlHelper

tvcustomerName = (By.ID, 'com.zhiyi.cxm.caixm_prep:id/tv_customer_name')

def check_add_customer(self):
    addedCustomerDisplay = self.driver.find_element(*self.tvcustomerName).text
    logging.info('新增客户输入展示的新增客户名字为：%s' % addedCustomerDisplay)
    sql = "select a.name,a.phone,a.plate_number_1,a.remark from cxm_bd_person a,cxm_bd_custom b where a.id=b.person_id order by a.id desc;"
    helper = MysqlHelper('47.103.62.98', 3306, 'cxm_service_data_base', 'cxmro', 'cxmtestro@20!*')
    customerName = str(helper.get_one(sql)[0])
    customerTel = str(helper.get_one(sql)[1])
    customerPlatenumber = str(helper.get_one(sql)[2])
    customerRemark = str(helper.get_one(sql)[3])
    logging.info('数据库查询的结果为：新增客户姓名：%s，新增客户电话：%s，新增客户车牌号：%s，在%s页面新增' % (customerName, customerTel, customerPlatenumber,customerRemark))
    try:
        assert customerName in addedCustomerDisplay, "新增成功"
        logging.info('新增客户断言成功')
    except AssertionError:
        logging.info('新增客户断言失败')
        return False
    else:
        return True

