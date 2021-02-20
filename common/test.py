from common.mysql_query import MysqlHelper

sql = "select a.name,a.phone,a.plate_number_1,a.remark from cxm_bd_person a,cxm_bd_custom b where a.id=b.person_id order by a.id desc;"
helper = MysqlHelper('47.103.62.98', 3306, 'cxm_service_data_base', 'cxmro', 'cxmtestro@20!*')
customerName = str(helper.get_one(sql)[0])
customerTel = str(helper.get_one(sql)[1])
customerPlatenumber = str(helper.get_one(sql)[2])
print(customerName,customerTel,customerPlatenumber)