import time
import HTMLTestRunner
import  unittest
import logging
from test_case import test_login
from test_case import test_cashierhomepage
from test_case import test_codelistcenter
from test_case import test_mainprocess
from test_case import test_repayment

def  test_report():
    # #指定测试用例和测试报告的路径
    # test_dir = '../test_case'

    # # #加载对应测试用例
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')
    # discover1 = unittest.defaultTestLoader.discover(test_dir, pattern='test_cashierhomepage.py')
    # discover2 = unittest.defaultTestLoader.discover(test_dir, pattern='test_codelistcenter.py')
    #
    # # # # 加载所有测试用例
    # # # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

    suite = unittest.TestSuite()
    #登录
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_login.LoginTest))
    # 主流程
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_mainprocess.MainprocessTest))
    #收银主页
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_cashierhomepage.Cashierhomepage))
    #还款操作
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_repayment.RepaymentTest))
    # 码单中心
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_codelistcenter.Codelistcenter))


    #定义报告的文件格式
    report_dir = '../reports'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_dir + '/' + now + ' test_report.html'

    #运行用例并生成测试报告
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner \
            (stream=f, title="Cxm Test Report", description="菜小秘专业版测试报告")
        logging.info("start run testcase...")
        runner.run(suite)

if __name__ == '__main__':
    test_report()