import unittest
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from TestCases.test import TestBrowser
import time
import os

# now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
# report_time = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime(time.time()))
# current_path = os.getcwd()  # 获取当前路径
# case_path = os.path.join(current_path, 'TestCate')  # 用例路径 可以多个
# report_path = os.path.join(current_path, 'Report')  # 结果报告存放路径
# report_title = (str(now) + '用例执行报告.html')
# result_path = os.path.join(report_path, report_title)

if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    while True:
        testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestBrowser))
        unittest.main()
    # desc = '用于展示修改样式后的HTMLTestRunner'
    # testsuite = unittest.TestSuite()
    # testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestBrowser))
    # with open(result_path, 'w', encoding='utf-8') as report:
    #     runner = HTMLTestRunner(stream=report,
    #                             title=report_title,
    #                             description=desc)
    #     runner.run(testsuite)
