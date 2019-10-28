import unittest
from BSTestRunner import BSTestRunner
import time, logging
import sys


path = r'D:\kyb'
sys.path.append(path)

test_dir = '../test_case'
report_dir = '../reports'

# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_register.py')
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir+'/'+now+'test_reprot.html'
with open(report_name, 'wb') as  f:
    runner = BSTestRunner(stream=f, title='kyb Test Reprot', description='kyb Android app test reprot')
    logging.info('start run test case....')
    runner.run(discover)


