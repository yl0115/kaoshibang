from common.myunit import StartEnd
from businessView.login_View import loginView
import logging
import unittest

class Login_Tes(StartEnd):
    csv_file = '../data/account.csv'
    # @unittest.skip('skip test1')
    def test1(self):
        logging.info('==================test1===============')
        lo = loginView(self.driver)
        data = lo.get_csv_data(self.csv_file, 1)
        lo.login_action(data[0], data[1])
        self.assertTrue(lo.check_LoginStaus())

    # @unittest.skip('skip test2')
    def test2(self):
        logging.info('==================test2===============')
        lo = loginView(self.driver)
        data = lo.get_csv_data(self.csv_file, 2)
        lo.login_action(data[0], data[1])
        self.assertTrue(lo.check_LoginStaus(), msg='login Fail')

    def test3(self):
        logging.info('=====================test3===============')
        lo = loginView(self.driver)
        data = lo.get_csv_data(self.csv_file, 3)
        lo.login_action(data[0], data[1])
        self.assertFalse(lo.check_LoginStaus(), msg='login Fail')

if __name__ == '__main__':
    unittest.main()
