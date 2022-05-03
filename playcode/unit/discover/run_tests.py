import unittest
import os

from matplotlib.cbook import report_memory
from HTMLTestRunner import HTMLTestRunner
import yagmail
import time

# 定义测试用例的目录为当前目录中test_case/目录
test_dir = '/Users/wyh/Desktop/二学期/selenium测试/playcode/unit/discover/test_case'

suits = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

def send_mail(report):

    yag = yagmail.SMTP(user="w1209574292@126.com", password="FJTSPUPVTENGFSPG", host='smtp.126.com')
    contents = ['This is wyh']
    yag.send('1209574292@qq.com', 'send email subject', contents,report)


if __name__ == '__main__':
    now_time=time.strftime("%Y-%m-%d %H_%M_%S")
    report=now_time+'result.html'
    fp=open(report,'wb')
    runner=HTMLTestRunner(stream=fp,verbosity=1)

    # runner = unittest.TextTestRunner()
    runner.run(suits)
    fp.close()
    send_mail(report)



