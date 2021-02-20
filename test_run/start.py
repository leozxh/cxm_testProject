#主运行

from test_run.report import test_report
from test_run.newstfile import newest_file
from test_run.sendmail import sendmail

if __name__ == '__main__':
    #运行测试用例，并生产测试报告
    test_report()
    #获取最新的测试报告路径，以及文件名:去reports里面拿最新的测试报告
    file_path,file_name =newest_file('..\\reports')


    #把最新的测试报告作为附件，发送邮件
    sender = '3331067370@qq.com'#发件前
    password = 'dbrnvplrradqciif'#授权码，非登录密码
    receiver = ['zhaxuanhuan@caixm.cn'] # 收件箱

    sendmail(sender,password,receiver,file_path,file_name)