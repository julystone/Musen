import time
import unittest

from common.HTMLTestRunnerNew import HTMLTestRunner
from common.Read_path import REPORT_DIR

report_path = REPORT_DIR

# 创建一个测试集合
suite = unittest.TestSuite()

# 创建一个执行器
runner = unittest.TextTestRunner()
loader = unittest.TestLoader()

# 添加测试用例
suite.addTest(loader.discover('./testcase', pattern='case*'))

date2display = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
with open(f'{report_path}report_{date2display}.html', 'wb') as fb:
    test_run = HTMLTestRunner(stream=fb, verbosity=2, title='py18_%s_report' % date2display,
                              description='参数化报告', tester='july')
    test_run.run(suite)

# runner.run(suite)
